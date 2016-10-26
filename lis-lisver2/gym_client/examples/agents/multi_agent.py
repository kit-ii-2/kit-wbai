import argparse
import six
from subprocess import Popen

parser = argparse.ArgumentParser()
parser.add_argument('--gpu', '-g', default=-1, type=int,
                    help='GPU ID (negative value indicates CPU)')
parser.add_argument('--log-file', '-l', default='reward', type=str,
                    help='reward log file name')
parser.add_argument('--agent-count', '-', default=1, type=int,
                    help='number of agent')
args = parser.parse_args()

for i in six.moves.range(args.agent_count):
    cmd = "python Lis_dqn.py --gpu={0} --log-file={1}".format(
        args.gpu, args.log_file +'_'+ str(i) + '.log')
    proc = Popen(cmd, shell=True)
    print("process id = %s" % proc.pid)

proc.wait()
