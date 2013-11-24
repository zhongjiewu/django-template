import os

from celery import chain

from match_engine.simitems.job_generate_index import JobGenerateIndex
from match_engine.simitems.job_rerank_candidates import JobRerankCandidates
from match_engine.simitems.job_search_candidates import JobSearchCandidates
from match_engine.simitems.job_tvrecfy import JobTvRecfy
from match_engine.datamodel.domain_descriptor import DomainDescriptor
from raas.tasks import run_job
from raas.tasks import convert_file


def compute_recommendation(uid, domain_name):

    dd = DomainDescriptor.from_db(uid, domain_name)
    data_root = dd.getDataPath()
    filename = "products.tsv" #dd.getDataFile()
    raw_file = os.path.join(data_root, filename)
    json_path = os.path.join(data_root, 'json')
    json_file = os.path.join(json_path, os.path.splitext(filename)[0] + ".json")
    tvrec_path = os.path.join(data_root, "domain_tvrec")
    search_path = os.path.join(data_root, "search")
    rank_path = os.path.join(data_root, "rank")
    chain(
        convert_file.s(True, raw_file, json_file) |
        run_job.s(JobTvRecfy, [json_path], tvrec_path) |
        run_job.s(JobGenerateIndex, [tvrec_path]) | 
        run_job.s(JobSearchCandidates, [tvrec_path], search_path) |
        run_job.s(JobRerankCandidates, [tvrec_path, search_path], rank_path)
    ).apply_async()
