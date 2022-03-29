def __df_boxplot_scatter(df,by,val):
    lst = []
    for i in range(len(val)):
        try:
            firstval = df.loc[:,by[i]].iloc[0]
        except KeyError:
            firstval = df.loc[:,by[i]].iloc[0][0]
        if isinstance(firstval,str):
            lst.append("(df_cp['{}']=='{}')".format(by[i],val[i]))
        else:
            lst.append("(df_cp['{}']=={})".format(by[i],val[i]))
    string = '&'.join(lst)
    return string

def df_boxplot_scatter(df:pd.DataFrame,column:str,by:list,dropnas=True,jitter=0,marker='o',mec='k',mfc='k',ls='',alpha=0.5,markersize=5,**kwargs):
    if dropnas:
        df_cp = df.dropna(how='all',axis=0,subset=column)
        df_cp = df_cp.dropna(how='any',axis=0,subset=by)
    else:
        df_cp = df
    if not isinstance(by,list):
        by = [by]
    plot = df_cp.plot(kind='box',column=column,by=by,showfliers=False)
    vals = sorted(textproc.unique(df_cp.loc[:,by].values))
    for i in range(len(vals)):
        val = vals[i]
        y = df_cp.loc[eval(__box_scatter(df_cp,by,val)),column]
        x = np.random.uniform(low=-jitter,high=jitter,size=len(y))+np.array([i+1]*len(y))
        plt.plot(x,y,marker=marker,mec=mec,mfc=mfc,markersize=markersize,ls=ls,alpha=alpha,**kwargs)
    return plot
