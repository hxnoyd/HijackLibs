#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import yaml
import pandas as pd

if __name__ == "__main__":

    #find-n-load
    yaml_files = glob.glob("../yml/**/*.yml", recursive=True)
    yaml_loaded = [yaml.safe_load(open(f).read()) for f in yaml_files]

    #flatten
    df = pd.DataFrame.from_dict(yaml_loaded)
    dfx = df.explode("ExpectedLocations").explode("VulnerableExecutables")
    dff = pd.concat([dfx.drop(['VulnerableExecutables'], axis=1), 
        dfx['VulnerableExecutables'].apply(pd.Series)], axis=1)

    #export
    dff[["Name", "ExpectedLocations", "Path", "Type", "PrivilegeEscalation", 
        "AutoElevate"]].to_csv("hijacklibs.csv", index=False)