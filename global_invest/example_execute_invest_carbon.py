# coding=UTF-8
# -----------------------------------------------
# Generated by InVEST 3.13.0 on Wed Jul 31 09:21:43 2024
# Model: Carbon Storage and Sequestration

import logging
import sys

import natcap.invest.carbon
import natcap.invest.utils

LOGGER = logging.getLogger(__name__)
root_logger = logging.getLogger()

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
    fmt=natcap.invest.utils.LOG_FMT,
    datefmt='%m/%d/%Y %H:%M:%S ')
handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[handler])

args = {
    'calc_sequestration': False,
    'carbon_pools_path': 'C:\\Users\\jajohns\\Files\\base_data\\invest_sample_data\\Carbon\\carbon_pools_willamette.csv',
    'discount_rate': '',
    'do_redd': False,
    'do_valuation': False,
    'lulc_cur_path': 'C:\\Users\\jajohns\\Files\\base_data\\invest_sample_data\\Carbon\\lulc_current_willamette.tif',
    'lulc_cur_year': '',
    'lulc_fut_path': '',
    'lulc_fut_year': '',
    'lulc_redd_path': '',
    'n_workers': '-1',
    'price_per_metric_ton_of_c': '',
    'rate_change': '',
    'results_suffix': '',
    'workspace_dir': 'C:\\Users\\jajohns\\Files\\base_data\\invest_sample_data\\Carbon\\output',
}

if __name__ == '__main__':
    natcap.invest.carbon.execute(args)