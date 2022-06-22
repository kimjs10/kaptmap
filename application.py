from flask import Flask, render_template
import boto3

application = Flask(__name__)


@application.route('/')
def home():
    map_html = get_s3_map_html()
    html_map = map_html.decode('utf-8')
    html_map = html_map.replace(
        '<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;">',
        '<div style="width:100%;height: 100%;"><div style="position:relative;width:100%;height: 100%;">')
    # print(html_map)
    # render_template() 내부 파라미터 작성하기
    return render_template("index.html", map=html_map)

def get_s3_map_html():
    #Creating Session With Boto3.
    session = boto3.Session(
        aws_access_key_id="AKIA2NJREBXTNX2VV4RY",
        aws_secret_access_key="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"
    )

    #Creating S3 Resource From the Session.
    s3 = session.resource('s3')
    obj = s3.Object('datago-kapt', 'data_map/map.html')
    return obj.get()['Body'].read()

if __name__ == '__main__':
    # application.debug = True
    application.run()