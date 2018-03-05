#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .sql import Sql
from JD.items import JdItem
import logging

class JDPipeline(object):

    def process_item(self, item, spider):
        # designed by yourself
        pass