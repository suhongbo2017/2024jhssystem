from flask import Flask ,render_template,request,flash,redirect,url_for
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap5
import server_connect
import pandas as pd
import write_mysql
import os
import secrets


app= Flask(__name__)
app.secret_key = secrets.token_hex(16)  # 16 字节的安全随机密钥

bootstrap= Bootstrap5(app)

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')


    
    
# 云海打印页面路由
@app.route('/yunHaiPrint',methods=['get','post'])
def yunHaiPrint():
    try:
        data= request.form.get("inputEntry")
        codeName= 1
        # print(data)
        if data:

            data= data.upper()
            seoutId= data
            data= data.split('/')
            print("格式化输入单号：",data)
            datas= pd.DataFrame()
            for ds in data:
                df= server_connect.query_SEord(ds,codeName)
                datas= pd.concat([datas,df])
            print('合并后的内容',datas)
            # for i,d in datas.iterrows():
            #     print(d['物料名称'])
            return render_template('yunHaiPrint.html',table= datas.iterrows(),data= seoutId)            
        else:
            datas= '查询出错，请输入查询'
            print(datas)            
            return render_template('yunHaiPrint.html')
    except Exception as e:
        print(f'{e}')       
        return render_template('yunHaiPrint.html')

# 精力打印页面路由
@app.route('/jinLiPrint',methods=['get','post'])
def jinLiPrint():
    try:
        data= request.form.get("inputEntry")
        codeName= 2
        # print(data)
        if data:

            data= data.upper()
            seoutId= data
            data= data.split('/')
            print("格式化输入单号：",data)
            datas= pd.DataFrame()
            for ds in data:
                df= server_connect.query_SEord(ds,codeName)
                datas= pd.concat([datas,df])
            print('合并后的内容')
            print(datas)


            
            # 备注等于物料名称以“膜”字分拆后列表中的第二个值。
            # datas.料号= datas.料号.str.split().str.get(1)
            # print('料号是',datas.料号)
            # datas['备注']= datas['物料名称'].str.split('膜').str.get(1)
            # # print('备注是',datas['备注'])
            # datas['整支规格新']= '(' + datas['整支规格'].str.split('*').str[1:3].str.join('*') + ')'
            # datas.整支规格= datas.整支规格 +'\n'+ datas.整支规格新
            # print("改后的",datas.整支规格)


            
           
            return render_template('jinLiPrint.html',table= datas.iterrows(),data= seoutId)            
        else:
            datas= '查询出错，请输入查询'
            print(datas)            
            return render_template('jinLiPrint.html')
    except Exception as e:
        print(f'{e}')       
        return render_template('jinLiPrint.html')
    
# 九茂送货单打印
@app.route('/jiuMaoPrint',methods=['get','post'])
def jiuMaoPrint():
    try:
        data= request.form.get("inputEntry")
        codeName= 3
        print('模板名称是',codeName)
        # print(data)
        if data:

            data= data.upper()
            seoutId= data
            data= data.split('/')
            print("格式化输入单号：",data)
            datas= pd.DataFrame()
            for ds in data:
                df= server_connect.query_SEord(ds,codeName)
                datas= pd.concat([datas,df])
            print('合并后',datas)
            # rows, a= datas.shape
            # if rows < 6:
            #     empty_rows= 6- rows
            #     empty_df= pd.DataFrame(index=range(empty_rows),columns=datas.columns)
            #     newData= pd.concat([datas,empty_df])
            #     print(newData)
            #     return render_template('jiuMaoPrint.html',table= newData.iterrows(),data= seoutId)    
            # if len(datas) < 6:
            #     datas.
            # for i,d in datas.iterrows():
            #     print(d['物料名称'])
            return render_template('jiuMaoPrint.html',table= datas.iterrows(),data= seoutId)            
        else:
            datas= '查询出错，请输入查询'
            print(datas)            
            return render_template('jiuMaoPrint.html')
    except Exception as e:
        print(f'{e}')       
        return render_template('jiuMaoPrint.html')


# 千吉打印页面路由
@app.route('/qianJi',methods=['get','post'])
def qianJi():
    try:
        data= request.form.get("inputEntry")
        codeName= 4
        # print(data)
        if data:

            data= data.upper()
            seoutId= data
            data= data.split('/')
            print("格式化输入单号：",data)
            datas= pd.DataFrame()
            for ds in data:
                df= server_connect.query_SEord(ds,codeName)
                # print('查询到的：',df)
                datas= pd.concat([datas,df])
            print('合并后的内容',datas)
            # for i,d in datas.iterrows():
            #     print(d['物料名称'])
            return render_template('qianJi.html',table= datas.iterrows(),data= seoutId)            
        else:
            datas= '查询出错，请输入查询'
            print(datas)            
            return render_template('qianJi.html')
    except Exception as e:
        print(f'{e}')       
        return render_template('qianJi.html')
    
@app.route('/zhidongli',methods=['get','post'])
def zhidongli():
    try:
        data= request.form.get("inputEntry")
        codeName= 2
        # print(data)
        if data:
            data= data.upper()
            seoutId= data
            data= data.split('/')
            print("格式化输入单号：",data)
            datas= pd.DataFrame()
            for ds in data:
                df= server_connect.query_SEord(ds,codeName)
                # print('查询到的：',df)
                datas= pd.concat([datas,df])
            print('合并后的内容')
            
            newdatas= datas.loc[:,[60,68,67,65,70,71,27]]
            # print(newdatas)
            new71= newdatas[71].str.split('*')
            import re
            newdatas['厚'],newdatas['宽'],newdatas['长'],newdatas['支']= [re.sub('[URM]','',x) for x in new71[0]]
            # print(newdatas['厚'],newdatas['宽'],newdatas['长'],newdatas['支'])
            newdatas.drop(71,inplace=True,axis=1)
            newdatas['订单号']= newdatas[60][0]
            newdatas['智动力编码']= newdatas[68][0]
            newdatas['品名']= newdatas[67][0]
            newdatas['数量']= newdatas[65][0]
            newdatas['数量']= newdatas['数量'].apply(lambda x :round(float(x),2))
            
            newdatas['批次号']= newdatas[70][0]
            newdatas['生产日期']= newdatas[27][0]
            newdatas['生产日期']= newdatas['生产日期'].dt.date
            
            print(newdatas.drop([60,68,67,65,70,27],inplace=True,axis=1))
            newdatas= newdatas.loc[:,['订单号','智动力编码','品名','宽','长','厚','支','数量','批次号']]
            print(newdatas)
            print(newdatas.columns)
            return render_template('zhidongli.html',tables= newdatas.to_dict(orient='records'),data= seoutId,names= newdatas.columns)            
        else:
            datas= '查询出错，请输入查询'
            print(datas)            
            return render_template('zhidongli.html')
    except Exception as e:
        print(f'{e}')       
        return render_template('zhidongli.html')

# 物料查询路由
@app.route('/queryMaterial',methods= ['get','post'])
def queryMateria():
    q_data= request.form.get('material')
    # num= 1
    print("输入的内容是",q_data)
    if q_data is None:
        return render_template('queryMaterial.html')

    #如果输入中包含“/”
    if '/' in q_data:
        q_data= q_data.split('/')
        print('多个查询中的第一个查询值是',q_data[0])
        datas= server_connect.queryMaterial(q_data[0])
        print('第二个查询值是',q_data[1])
        # print(datas.loc[(datas['物料名称'].str.contains(q_data[1])) and (datas['规格型号'].str.contains(q_data[1]))])
        result= datas.loc[(datas['物料名称'].str.contains(q_data[1])) | (datas['规格型号'].str.contains(q_data[1]))]
        print(22,result)
        return render_template('queryMaterial.html',datas= result.iterrows())
    
    
    datas= server_connect.queryMaterial(q_data)
    print('flask中',datas)
    if datas.empty:
        print('data is empty')
        message= '未查询到数据，请检查你的输入。'
        return render_template('queryMaterial.html',data= message)
        
    else:
        print('数据 is OK 这是本部数据')
        return render_template('queryMaterial.html',datas= datas.iterrows())
    
@app.route('/LSMqueryMaterial',methods= ['get','post'])
def LSMqueryMaterial():
    q_data= request.form.get('material')
    # num1= 2
    print("输入的内容是",q_data)
    if q_data is None:
        return render_template('LSMqueryMaterial.html')

    #如果输入中包含“/”
    if '/' in q_data:
        q_data= q_data.split('/')
        print('多个查询中的第一个查询值是',q_data[0])
        datas= server_connect.LSMqueryMaterial(q_data[0])
        print('第二个查询值是',q_data[1])
        # print(datas.loc[(datas['物料名称'].str.contains(q_data[1])) and (datas['规格型号'].str.contains(q_data[1]))])
        result= datas.loc[(datas['物料名称'].str.contains(q_data[1])) | (datas['规格型号'].str.contains(q_data[1]))]
        print(22,result)
        return render_template('LSMqueryMaterial.html',datas= result.iterrows())
    
    # 查询中只包含一个值
    datas= server_connect.LSMqueryMaterial(q_data)
    print('flask中',datas)
    if datas.empty:
        print('data is empty')
        message= '未查询到数据，请检查你的输入。'
        return render_template('LSMqueryMaterial.html',data= message)
        
    else:
        print('数据 is OK 这是LSM数据')
        return render_template('LSMqueryMaterial.html',datas= datas.iterrows())
    


@app.route('/Scheduled_Tasks')
def Scheduled_Tasks():

    sql_queryDate= "select 生产日期 from production_schedule ORDER BY DATE(生产日期) DESC "
    df_date= pd.read_sql(sql_queryDate,write_mysql.engine())
    df_datelist= df_date.生产日期.dt.date.unique()
    
    params= df_datelist[0]
    # params= '2023-12-20'
    print(params)
    sql_query= f"select * from production_schedule where date(生产日期) = '{params}'"
    
    df= pd.read_sql(sql_query,write_mysql.engine())
    if df.empty:
        message= '数据为空'
        return render_template('Scheduled_Tasks.html')
    column_names= ['id','生产日期','班次', '重点关注', '任务单号', '客户', '型号', '产品名称', '宽度', '长度', '涂布辊', '产能',
       '计划时间', '卷数', '计划米数', '订单交期', '订单数', '物料信息', '实际米数', '报废米数', '异常报废',
       '报废率', '实际生产时间', '平方数', '实际平方', '原膜批号', '生产批号', '机速', '剥离剂', 'F02',
       '7475胶带粘性', '涂布量1', '涂布量2', '涂布量3', '急测', '首件离型力1', '首件离型力2', '首件离型力3',
       '尾件离型力1', '尾件离型力2', '尾件离型力3', '熟化12H离型力1', '熟化13H离型力2', '熟化14H离型力3',
       '防静电值1', '防静电值2', '防静电值3', '常温24H离型力1', '常温24H离型力2', '常温24H离型力3',
       '烘烤70℃离型力1', '烘烤70℃离型力2', '烘烤70℃离型力3', '残率1', '残率2', '残率3', '原膜检查',
       '电晕值52达因', '电晕处理', '烘箱温度1', '烘箱温度2', '烘箱温度3', '烘箱温度4', '烘箱温度5', '烘箱温度6',
       '是否掉硅', '涂布问题描述', '正/反放卷', '涂头温度', '涂头湿度%', 'QC签名', '装刀距离', '速比', '气压',
       '一放张力', '放牵张力', '出牵张力', '收卷张力', '收卷锥度', '烘道张力', '生产领班', '备注']
    
    df.生产日期= df.生产日期.dt.date
    df.订单交期= df.订单交期.dt.date
    df.fillna('',inplace=True)
    # datas= df.to_dict(orient='records')
    df= df.iterrows()
    print(df)
    

    # print('打印DF',df)
    # print(len(df.columns),len(column_names))

    return render_template('Scheduled_Tasks.html',column_names= column_names,datas=df )
    # return render_template('Scheduled_Tasks.html',datas= df, columnsList= columnsList)
    

@app.route('/uploadFile',methods= ['get','post'])
def uploadFile():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File uploaded successfully')
            return redirect(url_for('upload_file'))
        else:
            flash('Invalid file type. Allowed file types are: txt, pdf, png, jpg, jpeg, gif')

#查询送货数量
@app.route('/query_seorder')
def query_seorder():
    #从页面获取开始日期与结束日期：startDate & endDate
    startDate= request.args.get('startDate')
    endDate= request.args.get('endDate')
    #如果返回结果为空，则返回查询页面
    if startDate is None or endDate is None:
        return render_template('query_seorder.html')
    print('查询页面中的开始日期和结束日期',startDate,endDate)
    
    #查询数据库中数据，以startData,endData为参数
    df= server_connect.seorder(startDate,endDate)
    #如果返回空值都输出一条message,并返回查询页面
    if df.empty:
        message= '未查询到数据，请检查你的输入。'
        return render_template('query_seorder.html',message= message)
    #设置columns为下面的列名
    df.columns= ['通知单内码','数据编号','数量','单价','金额','日期','订单号','品名','批号','规格']
    # print(df.日期)
    #设置日期格式为dt.date,单价为浮点数取3位小数，金额为浮点数取2位小数，数量为浮点数取2位小数
    df.日期= df.日期.dt.date
    df.单价= df.单价.apply(float).round(3)
    df.金额= df.金额.apply(float).round(2)
    df.数量= df.数量.apply(float).round(2)
    

    #使用df.loc对数据进行排序
    df= df.loc[:,['日期','订单号', '品名','单价','数量','金额','规格','批号']]
    # print(df.head())
    sum_df= df.金额.sum()/10000,'w'
    #使用pyecharts对数据进行绘图，并保存为html文件
    # from pyecharts.charts import Bar,Line
    # from pyecharts import options as opts

    # newdata= df.groupby('日期').agg({'金额':'sum','数量':'sum'})
    
    # print(newdata)
    # x_data= newdata.index.tolist()
    # y_data= newdata['金额'].tolist()
    # y2_data= newdata['数量'].tolist()
    # line= Bar(init_opts= opts.InitOpts(width='1500px',height='600px'))
    
    # line.add_xaxis(x_data)
    # line.add_yaxis('金额',y_data)
    # line.add_yaxis('数量',y2_data)
    # line.render('./static/report/line.html')
    return render_template('query_seorder.html',datas= df.iterrows(),names= df.columns,sum_df= sum_df)

@app.route('/5s')
def fiveS():
    return render_template('5s.html')

@app.route('/translate',methods= ['get','post'])
def translate():
    from PyDeepLX import PyDeepLX as dx
    import time
    strs= request.form.get('translate')
    lang= request.form.get('lang')
    print('lang is ',lang)
    print('text:',str(strs))
    time.sleep(1)
    try:

        if str is None:
            return render_template('translate.html')
        translate= dx.translate(strs,targetLang=lang)



        return render_template('translate.html',datas= translate,strs= strs)
    except Exception as e:
        print(e)
        return render_template('translate.html',datas= e,strs= strs)


if __name__ == '__main__':
    app.run(debug=True,host= "0.0.0.0", port=8080)