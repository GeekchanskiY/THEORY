In software engineering, version control is a class of systems responsible for managing changes to computer programs, documents, large web sites, or other collections of information. Version control is a component of software configuration management.

Most popular one is [[Git]]
## Common terminology
**Baseline**: An approved revision of a document or source file to which subsequent changes can be made.

**Blame**: A search for the author and revision that last modified a particular line.

**Branch**: A set of files under version control may be _branched_ or _forked_ at a point in time so that, from that time forward, two copies of those files may develop at different speeds or in different ways independently of each other.

**Change**: represents a specific modification to a document under version control. The granularity of the modification considered a change varies between version control systems.

**Checkout**: is to create a local working copy from the repository. A user may specify a specific revision or obtain the latest. The term 'checkout' can also be used as a noun to describe the working copy. When a file has been checked out from a shared file server, it cannot be edited by other users

**Clone**: _Cloning_ means creating a repository containing the revisions from another repository.

**Commit**: save changes, or saved changeset as a noun

**Conflict**: A conflict occurs when different parties make changes to the same document, and the system is unable to reconcile the changes.

**Delta compression**: retains only the differences between successive versions of files. This allows for more efficient storage of many different versions of files.

**Dynamic stream**: A stream in which some or all file versions are mirrors of the parent stream's versions.

**Locking**: no one else can update that file until it is unlocked. Locking can be supported by the version control system, or via informal communications between developers (aka _social locking_).

**Update**: An _update_ (or _sync_, but _sync_ can also mean a combined _push_ and _pull_) merges changes made in the repository (by other people, for example) into the local _working copy_.

**Export**: _Exporting_ is the act of obtaining the files from the repository. It is similar to _checking out_ except that it creates a clean directory tree without the version-control metadata used in a working copy.

**Fetch**: ~= pull. according to git, git pull copies changes from a remote repository directly into your working directory, while git fetch does not. The git fetch command only copies changes into your local Git repo. The git pull command does both.

**Initialize**: To create a new, empty repository.

**Head**: Also sometimes called _tip_, this refers to the most recent commit, either to the trunk or to a branch.

**Merge**: A _merge_ or _integration_ is an operation in which two sets of changes are applied to a file or set of files

**Pull/push**: Copy revisions from one repository into another. _Pull_ is initiated by the receiving repository, while _push_ is initiated by the source. _Fetch_ is sometimes used as a synonym for _pull_, or to mean a _pull_ followed by an _update_.

**Pull request**: merge request

**Repository**: data structure that stores metadata for set of files or directory structure

**Tag**: refers to an important snapshot in time, consistent across many files. These files at that point may all be tagged with a user-friendly, meaningful name or revision number.