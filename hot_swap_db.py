import sys
import argparse
import os

USERNAME = "aquarium"
PASSWORD = "aSecretAquarium"
DATABASE = "production"
DC_EXEC = ["docker-compose", "exec", "-T", "db"]

def get_args():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-d", "--dump",
                        help="dump sql database",
                        action="store_true")
    group.add_argument("-l", "--load",
                        help="load sql database",
                        action="store_true")
    parser.add_argument("-f", "--filename",
                        help="filename of database dump",
                        default="hot_swap.sql")
    return parser.parse_args()

def dump_cmd(filename):
    cmd = DC_EXEC
    cmd += ["mysqldump", "--no-tablespaces", "--user=" + USERNAME, "-p"]
    cmd += [DATABASE, ">", filename]
    return cmd

def load_cmd(filename):
    cmd = DC_EXEC
    cmd += ["mysql", "--user=" + USERNAME, "--password=" + PASSWORD]
    cmd += [DATABASE, "<", filename]
    return cmd

def main():
    args = get_args()
    cmd = []

    if args.dump:
        print("Dumping {} to {}.".format(DATABASE, args.filename))
        cmd = dump_cmd(args.filename)

    elif args.load:
        msg = "WARNING: This will overwrite the current database with the file {}."
        msg = "\033[93m" + msg + "\033[0m"
        print(msg.format(args.filename))
        proceed = input("Would you like to proceed? (y/n) ").lower()

        if proceed == 'y':
            print("Loading {} into {}.".format(args.filename, DATABASE))
            cmd = load_cmd(args.filename)

        else:
            print("Exiting")
            sys.exit()

    msg = os.system(' '.join(cmd))

    if msg == 0:
        print("Success!")

    else:
        print("Something went wrong.")

if __name__ == "__main__":
    main()
