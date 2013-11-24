from __future__ import absolute_import

from raas.celery_app import app
from raas.logic.file_adapter import tsv2json

@app.task(bind=True)
def run_job(self, ready, job, input, output=None, mode='local'):
    if not ready:
        return False

    print "----Start job {0}----".format(job.__name__)
    print "Input:", input
    print "Output:", output
    mr_job = job(args=['-r', mode, '--output', output] + input)
    with mr_job.make_runner() as runner:
        runner.run()
        print "Counter:",
        for counter in runner.counters():
            print counter,
        print '\n'
    print "----Finish job {0}----".format(job.__name__)

    return True


@app.task(bind=True)
def convert_file(self, ready, input, output, mode="tsv2json"):
    if not ready:
        return False
    print "----Start file conversion----"
    print "Input:", input
    print "Output:", output
    if mode=="tsv2json":
        tsv2json(input, output)
    print "---- Finish file conversion ----"
    return True
