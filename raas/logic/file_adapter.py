import json
from optparse import OptionParser

def tsv2json(infile, outfile):
    headers = []
    with open(infile) as inf, open(outfile, "w") as outf:
        first = True
        header_count= 0
        for line in inf:
            if first:
                headers = line.strip().split('\t')
                header_count = len(headers)
                print "{0} fields".format(header_count)
                first = False
                continue
            fields = line.rstrip('\n').split('\t')
            if len(fields) != header_count:
                print "**({0} fields, {1} fetched): {2}".format(header_count, len(fields), line)
                continue
            data = {}
            for k in xrange(header_count):
                if fields[k].strip():
                    data[headers[k]] = fields[k]

            outf.write("{0}\n".format(json.dumps(data)))


def json2tsv(infile, outfile):
    headers = set()
    with open(infile) as inf:
        for line in inf:
            dat = json.loads(line.strip())
            for k in dat.iterkeys():
                headers.add(k)
    headers_all = [h for h in headers]
    print "Total fields:", len(headers_all)
    count = 0
    with open(infile) as inf, open(outfile, "w") as outf:
        outf.write("{0}\n".format('\t'.join(headers_all)))
        for line in inf:
            dat = json.loads(line.strip())
            tsv_data = []
            for t in headers_all:
                if t in dat:
                    try:
                        tsv_data.append(dat[t].decode('ascii'))
                    except AttributeError:
                        tsv_data.append(str(dat[t]))
                    except UnicodeEncodeError:
                        tsv_data.append(unicode(dat[t]))
                    except UnicodeDecodeError:
                        tsv_data.append(unicode(dat[t].decode('utf-8')))
                    except Exception, e:
                        raise e
                else:
                    tsv_data.append(' ')
            line = tsv_data[0]
            for t in tsv_data[1:]:
                line += u'\t' + t.replace(u'\n', ' ').replace(u'\t', ' ')
            print >>outf, line.encode('utf-8')
            count += 1
            #outf.write("{0}\n".format(unicode(line)))
    print "Total lines:", count

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-f", "--from", dest="fromf")
    parser.add_option("-t", "--to", dest="tof")
    parser.add_option("-m", "--mode", dest="mode")

    (options, args) = parser.parse_args()
    if options.mode == "json2tsv":
        json2tsv(options.fromf, options.tof)
    else:
        tsv2json(options.fromf, options.tof)
