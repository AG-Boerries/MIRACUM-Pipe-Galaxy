MIRACUM workflows, data, scripts and configuration files for Galaxy
===================================================================

Prerequisites
-------------

This repo aims at providing all accessory files and documentation that you will
need to turn your Galaxy docker image into a productive Miracum variant calling
environment.

The documentation here does not go into much detail regarding the use
of docker (or podman), nor does it try to reproduce all of information about
Galaxy docker images.

To learn about all the features that Galaxy docker images have to offer, please
consult
`this documentation <https://github.com/bgruening/docker-galaxy-stable/blob/20.09/README.md>`_,
which applies to all "official" Galaxy docker images derived from
https://quay.io/repository/bgruening/galaxy.
At a bare minimum, it is recommended that you read the
`introductory section <https://github.com/bgruening/docker-galaxy-stable/blob/20.09/README.md#Usage>`_
of that guide. In particular you should understand the special role of the
``/export`` folder in the image.
`On-demand reference data with CVMFS <https://github.com/bgruening/docker-galaxy-stable/blob/20.09/README.md#cvmfs>`_
may be another section of special interest that you should have read before
installing reference data for your users (see the *Reference data* section
below). If you are upgrading your environment from an older Galaxy docker
image, the guide also features a section on
`Image upgrades <https://github.com/bgruening/docker-galaxy-stable/blob/20.09/README.md#Upgrading-images>`_.
Finally, if you are using the recommended Galaxy Miracum image please also take
a look at its specific
`usage hints <https://github.com/bgruening/docker-galaxy-exome-seq/blob/miracum_20.09/README.md>`_.


Getting the image ready for production use
------------------------------------------

Once you have pulled a suitable Galaxy image and have launched a container with
Galaxy you will have to do some initial setup work on your Galaxy instance to
prepare it for its users and their analysis needs.

This work will always involve installing *reference data*, *workflows* and
Miracum *annotation data*. In some situations you may also have to install
additional tools, or update existing ones.


Reference data
..............

The analyses carried out on your server will require human reference genome
data from various sources. Galaxy offers special tools called *data managers*,
which are only accessible to admin users, that can be used to pull this data
and make it available to regular users. Your first setup task will be to run
several of the data managers through Galaxy's graphical user interface, and our
page on `Installation of reference data <ref_data/README.md>`_ guides you
through this process.

Note: Just how many different data managers you will have to run depends on how
you started your container. By starting it in ``--privileged`` mode you will
enjoy automounting of some of the required reference data from the Galaxy
project's CVMFS servers as explained in the Galaxy docker image
`usage instructions <https://github.com/bgruening/docker-galaxy-stable/blob/20.09/README.md#cvmfs>`_.


Workflows
.........

This repo holds the **Galaxy Workflow files** that define the MIRACUM pipeline
used in Galaxy. To use these workflows, import the files into any Galaxy
instance that has all required tools installed (see Tools section below), and
make the workflows available to all users by publishing them on the instance.

For more details see the dedicated page on
`Installation of workflows <workflows/README.md>`_.


Annotation data
...............

In order to run the Miracum analysis workflows users will also need
Miracum-specific variants and gene annotation data. Similar to workflows, you
can make this data available to all users on a server through a shared history.
The process of doing so is detailed
`here <annotation_data/README.md>`_.

Users will start each analysis from a copy of the shared annotation data
history, or by copying the ``Miracum annotation data`` collection from that
history into a new history of their own.


Tools
.....

The simplest way to get a Galaxy instance with all required tools up and
running is to use our `preconfigured docker image
<https://github.com/bgruening/docker-galaxy-exome-seq/tree/miracum_20.09>`_. The current version
of this image can be pulled from
``quay.io/bgruening/galaxy-exome-seq:miracum_20.09``.
Basic usage instructions are available `here <https://github.com/bgruening/docker-galaxy-exome-seq/blob/miracum_20.09/README.md>`_.

For other instances of Galaxy, or if you would like to upgrade your list of
installed tools without downloading a new image version, please refer to our
`Installation of tools <tools/README.md>`_ page.


Advanced Galaxy configuration
.............................

Galaxy allows you to configure resource allocation for every single tool in the
workflows. A reasonable configuration matching your actual hardware resources
is essential for efficient data analysis.
You can find suggestions and hints `here <config/README.md>`_.


Information for contributors
----------------------------

Galaxy Workflow files are JSON-formatted. You can edit them manually, or import
them into Galaxy and use Galaxy's graphical workflow editor, then download the
edited version again. Either way, you should pretty-format the edited file
before committing them to obtain nicer, more readable diffs.
Use, *e.g.*, Python's built-in ``json.tool`` command for this task::

  python3 -m json.tool your_edited_workflow.ga > workflow_to_commit.ga
  
Python3.5 or later is required because earlier versions won't preserve element
order.

