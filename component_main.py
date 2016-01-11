'''
component_main.py

created 2 Mar 2015
@author: jrosner

'''

from kronos.utils import ComponentAbstract

class Component(ComponentAbstract):
    ''' component for running cufflinks program '''

    def __init__(self, component_name="run_cufflinks",
                 component_parent_dir=None, seed_dir=None):

        self.version = "1.0.0"

        ## initialize ComponentAbstract
        super(Component, self).__init__(component_name,
                                        component_parent_dir, seed_dir)


    def focus(self, cmd, cmd_args, chunk):
        pass


    def make_cmd(self, chunk=None):

        cmd        = self.requirements['cufflinks']
        cmd_args   = []

        for k, v in vars(self.args).iteritems():
            if v and (k in self.args):
                k = k.replace('_','-')
                if isinstance(v, bool):
                    cmd_args.extend(['--'+k])
                elif k == 'input':
                    infile = v
                else:
                    cmd_args.extend(['--'+k, v])

        cmd_args.append(infile)

        return cmd, cmd_args


## To run as stand alone
def _main():
    m = Component()
    m.args = component_ui.args
    m.run()

if __name__ == '__main__':
    import component_ui
    _main()

