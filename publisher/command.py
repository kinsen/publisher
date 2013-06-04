#!/usr/bin/env python
#*_* coding=utf8 *_*

import os
import subprocess

def execute(*cmd, **kwargs):
    """
    Helper method to execute command with optional retry.

    :cmd                Passed to subprocess.Popen.
    :process_input      Send to opened process.
    :check_exit_code    Defaults to 0. Raise exception.ProcessExecutionError
                        unless program exits with this code.
    :delay_on_retry     True | False. Defaults to True. If set to True, wait a
                        short amount of time before retrying.
    :attempts           How many times to retry cmd.
    :run_as_root        True | False. Defaults to False. If set to True,
                        the command is prefixed by the command specified
                        in the root_helper FLAG.

    :raises exception.Error on receiving unknown arguments
    :raises exception.ProcessExecutionError
    """

    process_input = kwargs.pop('process_input', None)
    attempts = kwargs.pop('attempts', 1)

    while attempts > 0:
        attempts -= 1
        try:
            print os.getcwd()
            print 'Running cmd (subprocess): %s' % ' '.join(cmd)
            _PIPE = subprocess.PIPE  # pylint: disable=E1101
            obj = subprocess.Popen(cmd,
                                   stdin=_PIPE,
                                   stdout=_PIPE,
                                   stderr=_PIPE,
                                   shell=False)
            result = None
            # pdb.set_trace()
            # time.sleep(2)
            # \

            if process_input is not None:
                result = obj.communicate("solidai\n")
                print result
                obj.stdin.write("solidai\n")
                obj.stdin.flush()
                # result = obj.communicate()
            else:
                result = obj.communicate()
            obj.stdin.close()  # pylint: disable=E1101
            _returncode = obj.returncode  # pylint: disable=E1101
            if _returncode:
                print 'Result was %s' % _returncode
            # print result
            return result
        except:
            if not attempts:
                raise
            else:
                print '%r failed. Retrying.' % cmd