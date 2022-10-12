import subprocess
import sys
from hashlib import md5, sha256
#from png import png_coll


def main():
    print("PNG Hash Collision Demo")

    fn1, fn2 = sys.argv[1:3]
    with open(fn1, "rb") as f:
        d1 = f.read()
    with open(fn2, "rb") as f:
        d2 = f.read()

    d1_hash = md5(d1).hexdigest()
    d2_hash = md5(d2).hexdigest()
    print("%s original file MD5 hash: %s" % (fn1, d1_hash))
    print("%s original filesize: %s kB" % (fn1, round(len(d1) / 1024)))
    print("%s original file MD5 hash: %s" % (fn2, d2_hash))
    print("%s original filesize: %s kB" % (fn1, round(len(d2) / 1024)))

    print("Colliding Files...")
    subprocess.run(["python", "png.py", fn1, fn2])

    with open("collision1.png", "rb") as f:
        coll_d1 = f.read()
    with open("collision2.png", "rb") as f:
        coll_d2 = f.read()

    coll_d1_hash = md5(coll_d1).hexdigest()
    coll_d2_hash = md5(coll_d2).hexdigest()
    print("%s collided file MD5 hash: %s" % (fn1, coll_d1_hash))
    print("%s collided filesize: %s kB" % (fn1, round(len(coll_d1) / 1024)))
    print("%s collided file MD5 hash: %s" % (fn2, coll_d2_hash))
    print("%s collided filesize: %s kB" % (fn1, round(len(coll_d2) / 1024)))

    print("Same files that cause MD5 collision hashed with SHA-256:")
    coll_d1_sha_hash = sha256(coll_d1).hexdigest()
    coll_d2_sha_hash = sha256(coll_d2).hexdigest()
    print("%s collided file SHA-256 hash: %s" % (fn1, coll_d1_sha_hash))
    print("%s collided file SHA-256 hash: %s" % (fn2, coll_d2_sha_hash))


if __name__ == "__main__":
    main()
