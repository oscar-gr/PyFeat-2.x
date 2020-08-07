# PyFeat-2.x: A Python-based Effective Feature Generation Tool from DNA, RNA, and Protein/Peptide Sequences
In Bioinformatics research, we usually noticed that using the same biological sequences and
even the same algorithms, but the performance varies a lot. Researchers unearth the riddle, it
is merely the different feature representation process. Feature representation techniques
drastically enhance the performance. We firmly do believe rational feature representation
techniques are a major significant contribution in Algorithomic-Bioinformatics and Machine
Learning in Biological Sciences research. The PyFeat–2.0 is an extensive Deep Learning friendly Python-based tool
for generating various numerical feature representation schemes from DNA, RNA, and protein primary structure sequences.

&nbsp;

### 1. Download Package
#### 1.1. Direct Download
We can directly [download](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/mrzResearchArena/PyFeat-2.x) by clicking the link.

**Note:** The package will download in zip format `(.zip)` named `PyFeat-2.x-master.zip`.

***`or,`***

#### 1.2. Clone a GitHub Repository (Optional)

Cloning a repository syncs it to our local machine (Example for Linux-based OS). After clone, we can add and edit files and then push and pull updates.
- Clone over HTTPS: `user@machine:~$ git clone https://github.com/mrzResearchArena/PyFeat-2.x.git `
- Clone over SSH: `user@machine:~$ git clone git@github.com:mrzResearchArena/PyFeat-2.x.git `

&nbsp;

##### Note #1: If the clone was successful, a new sub-directory appears on our local drive. This directory has the same name (PyFeat-2.x) as the `GitHub` repository that we cloned.

##### Note #2: We can run any Linux-based command from any valid location or path, but by default, a command generally runs from `/home/user/`.

##### Note #3: `user` is the name of our computer but your computer name can be different (Example: `/home/bioinformatics/`).


&nbsp;


### 2. Required Python Packages:
```
- Install: python (version >= 3.6)
- Install: numpy (version >= 1.15.0)
```

&nbsp;

### Table 1: Details Parameters/Arguments for the Features Generation
|   Argument     |   Argument (Shortcut) |    Variable Type     |   Default  | Choices            | Feature | Applicable | Help |
|     :---       |    :---:              |  :---:               |  :---:     | :---:              | :---:   | :---:      |  ---:|
| --seqType      | -seq                  | string               | -seq=PROT  | None  |:x:|:no_entry:|Please use either DNA, RNA, or PROTEIN (PROT). |
| --fasta        | -fa                   | string               |  None      | None | :x: |:no_entry:|Please enter the UNIX-like path. Example: -fa=/home/user/anyFASTA.fa |
| --terminusLength| -t                   | integer              | -t=30      | None | :x: |:no_entry:| The terminusLength 30 to 100  performed well. |
| --gGap         | -g                    | integer              | -g=5      | None | :x: |:no_entry:| The gap between 1 to 5 performed well. Example: -g=5  |
| --kTuple       | -k                    | integer              | -k=3      | None | :x: |:no_entry:| The k between 1 to 3 performed well. Example: -k=3  |
| --pseudoComposition | -pseudo          | integer |  -pseudo=0   | {1, 0} | :heavy_check_mark: |<ul><li>[x] DNA</li><li>[x] RNA</li><li>[x] PROT</li></ul>| 1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --monoMono          | -f11             | integer |  -f11=0      | {1, 0} | :heavy_check_mark: |<ul><li>[x] DNA</li><li>[x] RNA</li><li>[x] PROT</li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --monoDi            | -f12             | integer |  -f12=0      | {1, 0} | :heavy_check_mark: |<ul><li>[x] DNA</li><li>[x] RNA</li><li>[x] PROT</li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --diMono            | -f21             | integer |  -f13=0      | {1, 0} | :heavy_check_mark: |<ul><li>[x] DNA</li><li>[x] RNA</li><li>[x] PROT</li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --PSgGaps11         | -g11             | integer |  -g11=0      | {1, 0} | :heavy_check_mark: |<ul><li>[x] DNA</li><li>[x] RNA</li><li>[x] PROT</li></ul>| 1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --PSgGaps12         | -g12             | integer |  -g11=0      | {1, 0} | :heavy_check_mark: |<ul><li>[x] DNA</li><li>[x] RNA</li><li>[x] PROT</li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --PSgGaps21       | -g21               | integer |  -g12=0      | {1, 0} | :heavy_check_mark: |<ul><li>[x] DNA</li><li>[x] RNA</li><li>[x] PROT</li></ul>| 1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --PSkMers         | -psk               | integer |  -g21=0      | {1, 0} | :heavy_check_mark: |<ul><li>[x] DNA</li><li>[x] RNA</li><li>[x] PROT</li></ul>| 1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --binaryProfileFeature | -bpf     | integer |  -bpf=0      | {1, 0} | :heavy_check_mark: |<ul><li>[x] DNA</li><li>[x] RNA</li><li>[x] PROT</li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --BLOSUM62       | -blosum62        | integer |  -blosum62=0      | {1, 0} | :heavy_check_mark: |<ul><li>[x] PROT</li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --PAM250         | -pam250          | integer |  -pam250=0      | {1, 0} | :heavy_check_mark: |<ul><li>[x] PROT</li></ul>| 1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --physicochemicalProperties           | -pcp            | integer |  -bits=0      | {1, 0} | :heavy_check_mark: |<ul><li>[x] PROT</li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --BLASTn          | -blastn           | integer |  -blast=0      | {1, 0} | :heavy_check_mark: |<ul><li>[x] DNA</li><li>[x] RNA</li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |
| --transitionTransversion   | -tt              | integer |  -tv=0      | {1, 0} | :heavy_check_mark: |<ul><li>[x] DNA</li><li>[x] RNA</li></ul>|1 and 0 denotes (On/Active) and (Off/Deactivate) respectively. |


&nbsp;
&nbsp;


### 2. Generate Feature:
#### Example-1:
##### Generate only the `Binary Profile Feature`
``` console
user@machine:~$ python main.py -fa anyFASTA.fasta -bpf 1   # default: -seq PROT.
```

##### Generate only the `Binary Profile Feature` with the 40 terminus length.
``` console
user@machine:~$ python main.py -fa anyFASTA.fasta -bpf 1 -t 40   # default: -t 30.
```

&nbsp;

#### Example-2:
##### Generate only the `Position-wised g-Gaps & monoMono Style`
``` console
user@machine:~$ python main.py -fa anyFASTA.fasta -g11 1 # default: -t 30, -g 5, -k 3.
```
##### Generate only the `Position-wised g-Gaps & monoMono Style` with 3-gaps and 4-mers.
``` console
user@machine:~$ python main.py -fa anyFASTA.fasta -g11 1 -g 3 -k 4   # default: -t 30, -g 5, -k 3.
```

&nbsp;

#### Example-3:
##### Generate only the `transversion`
``` console
user@machine:~$ python main.py -fa anyFASTA.fasta -tt 1 -seq DNA # default: -seq PROT.
```
&nbsp;

#### Example-4:
##### Generate multiple dataset in a single command
``` console
user@machine:~$ python main.py -fa anyFASTA.fasta -bits 1 blosum62 1 pam250 1 g11 1
```

&nbsp;

**Note:** The PyFeat-2.x tool is able to generate multiple dataset with different parameters.

&nbsp;

### 3. Merge Feature:
#### Example-1:
##### Input Format:
```
user@machine:~$ python merge.py <anyFileName> <anyFileName.npy> <anyFileName.npy>
user@machine:~$ python merge.py <anyFileName> <anyFileName.npy> <anyFileName.npy> <anyFileName.npy>
```
&nbsp;

#### Example-2:
##### Merger Two File
```
user@machine:~$ python merge.py merge g11-16.npy g11-32.npy
```
&nbsp;

#### Example-3:
##### Merger Three File
```
user@machine:~$ python merge.py merge g11-16.npy g11-32.npy g11-32.npy
```

&nbsp;
**Note:** The PyFeat-2.x tool is able to merge the multiple datasets.
