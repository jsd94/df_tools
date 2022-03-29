import re
def standardize_vals(df,collapse_diffs=['case','typos','subsets']):
    for col in df.columns:
        std_vals = []
        lst = [val for val in df[col]]
        for string in lst:
            if not isinstance(string,str):
                continue
            if string not in std_vals:
                std_vals.append(string)
            else:
                continue
            
            
            if 'case' in collapse_diffs:
                string = string.lower()
                newlst = []
                for a in lst:
                    if isinstance(a,str):
                        newlst.append(a.lower())
                    else:
                        newlst.append(a)
                lst = newlst
            if 'subsets' in collapse_diffs:
                string = re.split(r':|\(',string)[0].strip()
                newlst = []
                for a in lst:
                    if isinstance(a,str):
                        newlst.append(re.split(r':|\(',a)[0].strip())
                    else:
                        newlst.append(a)
                lst = newlst
#             if 'typos' in collapse_diffs:

            matches = [0]*len(lst)
            for i in range(len(lst)):
                if lst[i] == string:
                    matches[i] = 1
            for j in range(len(lst)):
                if matches[j] == 1:
                    lst[j] = string
        df.loc[:,col] = lst
            
    return df
