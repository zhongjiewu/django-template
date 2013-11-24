# source this file to set the correct PYTHON path and DJANGO_SETTINGS_MODULE
# run:
#   source <this_file_name>
MAIN_APP_NAME=$(dirname $(ls */settings.py | head -n 1)| grep -o [^/]*$)
DIV="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export PYTHONPATH=$DIV:$PYTHONPATH
export DJANGO_SETTINGS_MODULE=$MAIN_APP_NAME.settings
export PS1=\[$MAIN_APP_NAME\]$PS1
