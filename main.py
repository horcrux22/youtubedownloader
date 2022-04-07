from utils import parse_opt
import ytdown

def main(arg):

    if 'list' in arg.url:
        print('playlist')
        return ytdown.playlist(arg)
    else:
        print('not playlist')
        return ytdown.not_playlist(arg)

if __name__ == '__main__':
    arg=parse_opt()
    main(arg)
