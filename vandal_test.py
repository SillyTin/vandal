# Standard lib imports
import sys
from os.path import abspath, dirname, join

# Prepend .. to $PATH so the project modules can be imported below
src_path = join(dirname(abspath(__file__)), "..")
sys.path.insert(0, src_path)

# Local project imports
import src.exporter as exporter
import src.dataflow as dataflow
import src.tac_cfg as tac_cfg
import src.settings as settings

if __name__ == '__main__':

    f = open('/root/projects/evm_decompiler/1/func_call/func_call.bin','r')
    settings.import_config(settings._CONFIG_LOC_)
    cfg = tac_cfg.TACGraph.from_bytecode(f)
    print("Initial CFG generation completed.")
    dataflow.analyse_graph(cfg)
    exporter.CFGDotExporter(cfg).export('cfg.pdf')