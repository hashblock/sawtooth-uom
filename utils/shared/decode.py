# ------------------------------------------------------------------------------
# Copyright 2018 Frank V. Castellucci and Arthur Greef
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------------

"""Decode - Support hashblock module

This module is referenced when there is a need to decode a state
address. It also includes other sundry utilities
"""


def decode_address(address):
    return {
        'family': 'match',
        'address': address,
        'dimension': 'UTXQ',
        'exchange': 'ask',
        'data': '5 bags of peanuts'}
