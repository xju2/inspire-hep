

if __name__ == "__main__":
    import os
    import argparse
    import arxiv
    from citations import citations

    parser = argparse.ArgumentParser(description="get bib for a list of articles")
    add_arg = parser.add_argument
    add_arg("filename", help='input file containing arxiv ids')
    add_arg("-t", "--type", help='entry information', default='arxiv', choices=['inspire', 'arxiv'])
    add_arg("-d", "--debug", action='store_true', help="in a debug mode")
    args = parser.parse_args()

    filename = args.filename
    debug = args.debug
    info_type = args.type
    if not os.path.exists(filename):
        print(f"{filename} does not exit.")
        exit(0)

    print(f"Input information type: {info_type}")
    with open(filename, 'r') as f:
        if info_type == 'arxiv':
            inspire_ids = [arxiv.find_index(line[:-1]) for line in f]
        else:
            inspire_ids = [line[:-1] for line in f]
    
    import time
    time_stamp = time.strftime('%Y%m%d-%H%M%S', time.localtime())

    out_bib = ""
    columns = [
        "texkeys", 'arxiv_eprints', 'preprint_date', 'citation_count',
        "citation_count_without_self_citations", 'doi', 'title']
    data = []

    for inspire_id in inspire_ids:
        print("procesing {}".format(inspire_id))
        try:
            if info_type == "arxiv":
                res = citations('arxiv', inspire_id, debug=debug)
            else:
                res = citations('literature', inspire_id)
        except Exception as inst:
            print(type(inst), inst.args)
            print("Skipping {}".format(inspire_id))
            continue

        info = [str(res[x]) for x in columns]
        info[-1] = '"{}"'.format(info[-1])
        data.append(info)
        out_bib += res['bibtex'] + "\n"


    print(out_bib)