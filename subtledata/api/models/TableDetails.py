#!/usr/bin/env python
"""
Copyright 2012 Wordnik, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
class TableDetails:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'pos_table_id': 'str',
            'subtledata_id': 'int',
            'revenue_center_name': 'str',
            'revenue_center_id': 'int',
            'open_tickets': 'list[OpenTicket]',
            'name': 'str'

        }


        #Table Identifier
        self.pos_table_id = None # str
        #Table ID
        self.subtledata_id = None # int
        #Revenue Center Name
        self.revenue_center_name = None # str
        #Revenue Center ID
        self.revenue_center_id = None # int
        self.open_tickets = None # list[OpenTicket]
        #Table Name
        self.name = None # str
        
