#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch

from source_cli_demo import SourceCliDemo

if __name__ == "__main__":
    source = SourceCliDemo()
    launch(source, sys.argv[1:])
