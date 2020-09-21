MIRACUM workflows, scripts and configuration files for Galaxy
=============================================================

Galaxy Admins
-------------

Workflows
.........

This repo holds the **Galaxy Workflow files** that define the MIRACUM pipeline
used in Galaxy. To use these workflows, import the files into any Galaxy
instance that has all required tools installed (see Tools section below), and
make the workflows available to all users by publishing them on the instance.

Users can then run the *Miracum - main*, *Miracum - variant annotation* and
*Miracum - report variants* workflows (or their *panel* counterparts), in this
order, to go from raw sequenced exome reads to annotated tabular variant
reports.

Note: If you're not planning to edit the workflows, there is no need for you to
import any `Galaxy_Subworkflow_*.ga` workflow definition files since the main
workflows have the subworkflows integrated into their definition files.

Tools
.....

The simplest way to get a Galaxy instance with all required tools up and
running is to use our `<https://github.com/bgruening/docker-galaxy-exome-seq>
preconfigured docker image`_. The current version of this image can be pulled
from ``quay.io/bgruening/galaxy-exome-seq:miracum_19.01``.

For other instances of Galaxy, you can use the `miracum_tools.yaml` file, which
is part of this repo, to install all required tools at the expected versions
with
`<https://training.galaxyproject.org/training-material/topics/admin/tutorials/tool-management/tutorial.html>
Ephemeris`__.

Advanced Galaxy configuration
.............................

Galaxy allows you to configure resource allocation for every single tool in the
workflows. This is done via a `job_conf.xml` configuration file.

You can read more about the syntax and options available in this config file in
the corresponding `<https://docs.galaxyproject.org/en/master/admin/jobs.html>
section of the Galaxy documentation`__.

For the Miracum project specifically, this repo includes a
`job_conf.xml.sample` file, with what we think are reasonable default settings
for the workflows. The sample file assumes SLURM as your job scheduler (which
comes included and completely set up with our docker image) and allocates
multiple cores to the tools that profit from them.

Of course, you may need to tailor the exact settings to your hardware resources
or cluster specifications.

To use the new configuration, copy the sample file to `config/job_conf.xml`
inside the Galaxy root folder. If you're using our docker image that place is
`/export/galaxy-central/config/job_conf.xml` from inside the container (you can
also put the file in a different location, as long as that location is
accessible from inside the container, and point Galaxy to this file by
including `-e GALAXY_CONFIG_JOB_CONFIG_FILE=<path_to_the_job_conf_file>` in
your container *run* command.


Developers
----------

Galaxy Workflow files are JSON-formatted. You can edit them manually, or import
them into Galaxy and use Galaxy's graphical workflow editor, then download the
edited version again. Either way, you should pretty-format the edited file
before committing them to obtain nice and readable diffs.
Use, *e.g.*, Python's built-in ``json.tool`` command for this task::

  python3 -m json.tool your_edited_workflow.ga > workflow_to_commit.ga
  
Python3.5 or later is required because earlier versions won't preserve element
order.

When you edit a subworkflow, please note that the changes you make do not get
reflected in the containing workflow (which carries its own embedded copy of
the subworkflow). To make your changes visible in the containing workflow, you
need to remove the embedded subworkflow from it and add the edited version back
in.

