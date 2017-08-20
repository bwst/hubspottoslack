import csv
import os
from datetime import datetime

import hubspot



def main():
    tempData = []
    pipelines = hubspot.api.fetch_pipelines()
    for pipeline in pipelines:
        deals = hubspot.api.fetch_deals()
        print('Pipeline: %s, id: %s' %(pipeline.get_label(), pipeline.get_id()))
        pipeline_id = pipeline.get_id()
        if pipeline_id is not None:

            deals = [deal for deal in deals if deal.get_pipeline_id() == pipeline_id]
            print([deal.get_stage().data for deal in deals])


if __name__ == '__main__':
    main()
