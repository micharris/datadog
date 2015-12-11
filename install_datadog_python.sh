#!/bin/bash
 
if [[ ! -d datadog/bin ]]; then
 ${LOCAL_PYTHON}/virtualenv datadog
fi
cd datadog
source bin/activate
pip install datadog
pip install requests