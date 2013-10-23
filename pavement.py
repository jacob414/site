# -*- coding: utf-8 -*-

import os
import sys

import paver
from paver.easy import *

from plexical import shortcuts
from plexical.px.util import script, check, subst

settings = {
    'REMOTE': 'wf:~/webapps/jacob414',
    'EXCLUDES': '--exclude=.* --exclude=*.py --exclude=\.#*'
}

expand = lambda txt: subst(txt, **settings)

path = lambda *segs: shortcuts.path(*[expand(s) for s in segs])

sh = lambda line: paver.easy.sh(expand(line))

@task
def deploy():
    sh('rsync -ar * wf:~/webapps/jacob414')
