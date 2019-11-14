import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--config',default='ds_config')
    parser.add_argument('-s','--spider',help = 'this is spider',default='spider_example')
    parser.add_argument('-t','--thread_count',help='this is thread count',default=0, type=int)
    parser.description = "this is my parse example"
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    print(args.config)
    print(args.spider)
    print(args.thread_count)
