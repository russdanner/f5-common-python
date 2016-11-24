# coding=utf-8
#
# Copyright 2015-2016 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from f5.bigip.resource import AsmResource
from f5.bigip.resource import Collection
from f5.bigip.resource import UnsupportedOperation


class Signature_Statuses_s(Collection):
    """BIG-IP® ASM Signature Statuses collection."""
    def __init__(self, asm):
        super(Signature_Statuses_s, self).__init__(asm)
        self._meta_data['object_has_stats'] = False
        self._meta_data['allowed_lazy_attributes'] = [Signature_Status]
        self._meta_data['attribute_registry'] = {
            'tm:asm:signature-statuses:signature-statusstate':
                Signature_Status}


class Signature_Status(AsmResource):
    """BIG-IP® ASM Signature Status resource"""
    def __init__(self, signature_statuses_s):
        super(Signature_Status, self).__init__(signature_statuses_s)
        self._meta_data['required_json_kind'] =\
            'tm:asm:signature-statuses:signature-statusstate'

    def create(self, **kwargs):
        """Create is not supported for Signature Status resource

                :raises: UnsupportedOperation
        """
        raise UnsupportedOperation(
            "%s does not support the create method" % self.__class__.__name__
        )

    def delete(self, **kwargs):
        """Delete is not supported for Signature Status resource

                :raises: UnsupportedOperation
        """
        raise UnsupportedOperation(
            "%s does not support the delete method" % self.__class__.__name__
        )

    def modify(self, **kwargs):
        """Modify is not supported for Signature Status resource

                :raises: UnsupportedOperation
        """
        raise UnsupportedOperation(
            "%s does not support the modify method" % self.__class__.__name__
        )
