from argparse import ArgumentParser
from DBAdd import DBAdd

def main():
    argparser = ArgumentParser(description="A CLI to add buckets to the bucket scanning project")
    argparser.add_argument("-b",action="store",required=True,help="This is the bucket name... not the url to the "
                                                                  "bucket just the bucket's name")
    argparser.add_argument("-p",action="store",required = True,help="Represents the product that the bucket was "
                                                                    "scraped from. This should be the google play "
                                                                    "package name com.something.somethingcool")
    argparser.add_argument("-c",action="store",required = False,help="Represents the company that owns the bucket "
                                                                     "and/or product. The primary purpose of this "
                                                                     "data is to determine eligibility for bug bounty "
                                                                     "programs")

    args = argparser.parse_args()
    db = DBAdd()
    db.add_bucket(args.b,args.p,args.c)