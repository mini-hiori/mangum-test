# mangum-test
- FastAPIをLambdaにするやつ(mangum)を使ってみる
- ServerlessFrameworkでLambda+APIGatewayをデプロイしてみる
    - 両方とも成功済み

## できるもの
- 普通のserverless-apiができます
![](https://raw.githubusercontent.com/mini-hiori/mangum-test/main/docs/architecture.png)

## つかいかた
1. ECRを手動で作成
2. [いつものアレ](https://dev.classmethod.jp/articles/github-action-ecr-push/)にてECRにコンテナをアップロード
3. SSMパラメータストアにAWSアカウントIDとECR上のコンテナイメージダイジェストを登録
4. serverlessframeworkのインストール+初期設定を[ここ](https://dev.classmethod.jp/articles/easy-deploy-of-lambda-with-serverless-framework/)を参考に行う
    - ポリシーはAdministratorAccessの代わりに以下をアタッチ。これらは作るリソースがあるため必須っぽい
        - IAMFullAccess
        - AmazonEC2ContainerRegistryFullAccess
        - AmazonS3FullAccess
        - CloudWatchLogsFullAccess
        - AmazonAPIGatewayAdministrator
        - AmazonSSMReadOnlyAccess
        - AWSCloudFormationFullAccess
        - AWSLambda_FullAccess
5. serverlessframeworkを実行(sls deploy)。特に問題なければAPIのURLが吐き出されて実行できるようになる