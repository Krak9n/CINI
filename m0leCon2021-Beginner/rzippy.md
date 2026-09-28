We are handed **999.bz2** file. The first step is to decode it with bzip2.  
```bash
bzip2 -dk 999.bz2
```
---

We get `999` file which I renamed to 998. It is another .bz2 archive. Decompress it.

---

There wasn't much given but xxd gave a clue. Magic bytes were `4d53 5749 4d00` which are used for MSWIM files. Conclussion: I was given a .wim.   
Before even running some external utilities I also gave a look at the tail:
```bash
.<.W.I.M.>
.<.T.O.T.A.L.B.Y.T.E.S.>.3.2.6.1.9.1.<./.T.O.T.A.L.B.Y.T.E.S.>
.<.I.M.A.G.E. .I.N.D.E.X.=.".1.".>
.<.N.A.M.E.>.1.<./.N.A.M.E.>
.<.D.I.R.C.O.U.N.T.>.0.<./.D.I.R.C.O.U.N.T.>
.<.F.I.L.E.C.O.U.N.T.>.1.<./.F.I.L.E.C.O.U.N.T.>
.<.T.O.T.A.L.B.Y.T.E.S.>.3.2.5.6.3.5.<./.T.O.T.A.L.B.Y.T.E.S.>
.<.C.R.E.A.T.I.O.N.T.I.M.E.>
.<.H.I.G.H.P.A.R.T.>.0.x.0.1.D.7.A.A.7.6.<./.H.I.G.H.P.A.R.T.>
.<.L.O.W.P.A.R.T.>.0.x.E.D.7.1.1.F.6.E.<./.L.O.W.P.A.R.T.>
.<./.C.R.E.A.T.I.O.N.T.I.M.E.>
.<.L.A.S.T.M.O.D.I.F.I.C.A.T.I.O.N.T.I.M.E.>
.<.H.I.G.H.P.A.R.T.>.0.x.0.1.D.7.A.A.7.6.<./.H.I.G.H.P.A.R.T.>
.<.L.O.W.P.A.R.T.>.0.x.E.D.7.1.1.F.6.E.<./.L.O.W.P.A.R.T.>
.<./.L.A.S.T.M.O.D.I.F.I.C.A.T.I.O.N.T.I.M.E.>
.<./.I.M.A.G.E.>
.<./.W.I.M.>.
```

The most important thing here is the **filecount**. There was an image inside.  

As a prideful Arch Linux user I installed [wimlib package]() and started digging into the file.
```bash
> wiminfo
WIM Information:
----------------
Path:           998.out
GUID:           0xb09a28457a64601660c52624475ab01a
Version:        68864
Image Count:    1
Compression:    None
Chunk Size:     0 bytes
Part Number:    1/1
Boot Index:     0
Size:           326191 bytes
Attributes:     Relative path junction

Available Images:
-----------------
Index:                  1
Name:                   1
Description:
Directory Count:        0
File Count:             1
Total Bytes:            325635
Hard Link Bytes:        0
Creation Time:          Wed Sep 15 21:16:19 2021 UTC
Last Modification Time: Wed Sep 15 21:16:19 2021 UTC
WIMBoot compatible:     no
```
File confirmed.
Now just mount it with rw option and extract the file.  
```bash
> sudo wimmountrw 998.out .
> sudo wimapply 998.out .
```
And after that we get our **1/** directory with a 995 file inside.
File is without the format so we should first run yet again exiftool on it and rename to appropriate .gz. Then just extract with gzip, and we get another 995 file which is a MSWIM file.

