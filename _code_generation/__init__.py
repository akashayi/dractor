# Copyright (C) 2017 Verizon. All Rights Reserved.
#
#     File:    __init__.py
#     Author:  Phil Chandler
#     Date:    2017-02-17
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""
The code here is used to generate the code that is delivered from the project.
It is not intended to be shipped with the project's Python package.
"""

from .mof2py import MOFTranslator
