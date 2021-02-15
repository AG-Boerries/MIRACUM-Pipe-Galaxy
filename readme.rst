MIRACUM workflows, data, scripts and configuration files for Galaxy
===================================================================

Galaxy Admins
-------------

Workflows
.........

This repo holds the **Galaxy Workflow files** that define the MIRACUM pipeline
used in Galaxy. To use these workflows, import the files into any Galaxy
instance that has all required tools installed (see Tools section below), and
make the workflows available to all users by publishing them on the instance.

Registered users can then find these workflows by selecting
``Shared Data`` -> ``Workflows`` from Galaxy's top menu. This brings up a
complete list of published workflows on your server, from which users can
directly run any workflow by selecting the "arrow-down" expanding menu next to
the workflow's name.

Please note that directly running the shared workflows is strongly preferable
over importing them first into a user's personal workflow list. Importing
would create a user-specific *copy* of the workflow, which would get
out-of-sync with the latest available version over time as workflow updates
become available.

=> **Running shared workflows directly from the ``Published Workflows`` list
ensures that all users are always using the latest version of any workflow.**


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

For other instances of Galaxy, you can use the `miracum_tools.yaml` file, which
is part of this repo, to install all required tools at the expected versions
with `Ephemeris
<https://training.galaxyproject.org/training-material/topics/admin/tutorials/tool-management/tutorial.html>`__.


Advanced Galaxy configuration
.............................

Galaxy allows you to configure resource allocation for every single tool in the
workflows. This is done via a `job_conf.xml` configuration file.

You can read more about the syntax and options available in this config file in
the corresponding `section of the Galaxy documentation
<https://docs.galaxyproject.org/en/master/admin/jobs.html>`__.

For the Miracum project specifically, this repo includes a
``job_conf.xml.sample`` file, with what we think are reasonable default settings
for the workflows. The sample file assumes SLURM as your job scheduler (which
comes included and completely set up with our docker image) and allocates
multiple cores to the tools that profit from them.

Of course, you may need to tailor the exact settings to your hardware resources
or cluster specifications.

To use the new configuration, copy the sample file to ``config/job_conf.xml``
inside the Galaxy root folder. If you're using our docker image that place is
``/export/galaxy-central/config/job_conf.xml`` from inside the container (you
can also put the file in a different location, as long as that location is
accessible from inside the container, and point Galaxy to this file by
including ``-e GALAXY_CONFIG_JOB_CONFIG_FILE=<path_to_the_job_conf_file>`` in
your container *run* command.


Developers
----------

Galaxy Workflow files are JSON-formatted. You can edit them manually, or import
them into Galaxy and use Galaxy's graphical workflow editor, then download the
edited version again. Either way, you should pretty-format the edited file
before committing them to obtain nicer, more readable diffs.
Use, *e.g.*, Python's built-in ``json.tool`` command for this task::

  python3 -m json.tool your_edited_workflow.ga > workflow_to_commit.ga
  
Python3.5 or later is required because earlier versions won't preserve element
order.

