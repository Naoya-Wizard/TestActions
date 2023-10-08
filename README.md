
# GitHub Actionsガイド

## GitHub Actionsとは？

GitHub Actionsは、GitHubのリポジトリ内でCI（Continuous Integration）/ CD（Continuous Delivery）ワークフローを自動化するためのツールです。これにより、コードの変更をリモートリポジトリにプッシュするたびに、定義したタスク（例: テストの実行、ビルドの作成、デプロイなど）が自動的に実行されます。

GitHub Actionsの主な特徴は以下の通りです：

1. **統合**: GitHub ActionsはGitHubのコアサービスとして提供されるため、追加のセットアップやサービスが不要です。
2. **ワークフローファイル**: ユーザーは、リポジトリの`.github/workflows`ディレクトリ内のYAMLファイルにワークフローを定義します。
3. **カスタマイズ可能**: ユーザーは、様々なランナー（実行環境）上でジョブを実行したり、さまざまなアクションを組み合わせてワークフローを構築することができます。
4. **マトリックスビルド**: 複数のバージョンや設定でのテストやビルドを同時に実行することができます。
5. **無料の利用枠**: 公開リポジトリでは、無料で多くの分の実行時間が提供されます。

以上の特徴を活かして、GitHub Actionsはソフトウェア開発のワークフローを効率的に自動化する強力なツールとして広く利用されています。

## GitHub Actionsのセットアップ

### なぜ必要か？
GitHub Actionsは、特定のGitHubイベント（例: プルリクエストの作成）がトリガーされたときに自動的に実行するタスクを定義するための機能です。

1. リポジトリに移動し、**Actions**タブをクリックします。
2. **New workflow**をクリックし、**set up a workflow yourself**を選択します。
3. ワークフローファイル（例: Slackにメッセージを送る）を以下のように編集します:

```
name: Slack Notification for PR

on:
  pull_request:
    types: [opened]

jobs:
  slack_notification:
    runs-on: ubuntu-latest
    steps:
    - name: Send Slack Notification
      uses: act10ns/slack@v1
      with:
        status: ${{ job.status }}
        steps: ${{ toJson(steps) }}
        channel: '#your-channel-name'
        mention: 'usergroup'
        token: ${{ secrets.SLACK_WEBHOOK_URL }}
```

4. このファイルを保存し、コミットします。

## シークレットの追加

### なぜ必要か？
シークレットは、公開したくない情報（例: APIキー、トークンなど）を安全に保存するための機能です。GitHub Actionsの中でこれらの情報を使用する場合、シークレットとして保存するのがベストプラクティスです。

1. リポジトリに移動し、**Settings**タブをクリックします。
2. 左側のメニューから**Secrets**を選択します。
3. **New repository secret**をクリックします。
4. **Name**に`SLACK_WEBHOOK_URL`と入力し、**Value**に先ほどコピーしたSlackのWebhook URLをペーストします。
5. **Add secret**をクリックして保存します。

## GitHub Actionsのワークフローファイルのセクションの説明

### `name:`

- **目的**: ワークフローの名前を指定します。
- **動作**: GitHubのActionsタブ内での識別のために使われます。

### `on:`

- **目的**: このワークフローがどのGitHubのイベントに対してトリガーされるかを指定します。
- **動作**: この例では、新しいプルリクエストが開かれたときにワークフローがトリガーされます。

### `jobs:`

- **目的**: 1つ以上のジョブを定義します。ジョブは独立して、または他のジョブに依存して実行されるタスクのグループです。
- **動作**: この例では、`slack_notification`という名前のジョブが1つ定義されています。

### `runs-on:`

- **目的**: ジョブが実行されるGitHub Actionsのランナータイプを指定します。
- **動作**: この例では、最新のUbuntuランナー上でジョブが実行されます。

### `steps:`

- **目的**: ジョブ内で実行される一連のタスクを定義します。
- **動作**: この例では、Slackに通知を送るステップが1つ含まれています。

### `uses:`

- **目的**: ステップで使用されるアクションを指定します。
- **動作**: この例では、Slackに通知を送るための`act10ns/slack@v1`というアクションが使用されています。

### `with:`

- **目的**: アクションのパラメータや入力を定義します。
- **動作**: この例では、Slackのチャンネル、メンションのタイプ、そしてWebhook URLなどのパラメータが指定されています。

## act10ns/slack@v1とは？

`act10ns/slack@v1`は、GitHub ActionsからSlackにメッセージを送信するためのアクションです。このアクションを使用することで、GitHubのワークフロー内から直接Slackチャンネルに通知を送ることができます。

主な特徴として：

1. **シンプルな設定**: SlackのWebhook URLを指定するだけで、簡単にSlackにメッセージを送信することができます。
2. **カスタマイズ可能**: メッセージの内容やフォーマット、メンションするユーザーやグループなど、さまざまなオプションをカスタマイズすることができます。
3. **ジョブのステータスに基づく通知**: 成功、失敗、キャンセルなど、ジョブの実行結果に応じて異なるメッセージやアラートをSlackに送信することができます。

`act10ns/slack@v1`を使用することで、GitHub Actionsのワークフローの重要なイベントや結果をリアルタイムでSlackチャンネルに通知し、開発チーム全体が即座に情報を受け取ることができます。

## act10ns/slack@v1の他の類似アクション

GitHub Actionsのマーケットプレイスには、Slackに通知を送るための他のアクションも多数存在します。以下はその中の一部の例です：

1. **[Slack Notification Action](https://github.com/marketplace/actions/slack-notification-action)**
   - このアクションは、様々なイベントに応じてSlackにカスタムメッセージを送信することができます。
   - メッセージのカスタマイズや、特定の条件下でのみ通知を送ることなど、高度な設定が可能です。

2. **[Slackify](https://github.com/marketplace/actions/slackify)**
   - Slackifyは、GitHub ActionsのログをSlackに送信するためのアクションです。
   - ワークフローの実行中の詳細なログをリアルタイムでSlackに通知することができます。

3. **[Slack Action](https://github.com/marketplace/actions/slack-action)**
   - このアクションは、特定のメッセージフォーマットやアタッチメントを使用してSlackに通知を送ることができます。
   - ジョブの結果や成果物のリンクなど、様々な情報をSlackに送信することができます。

これらのアクションを選択する際は、自分のニーズやプロジェクトの要件に合わせて適切なものを選ぶことが重要です。GitHubのマーケットプレイスでは、これらのアクションのドキュメントや評価、ユーザーのフィードバックを確認することができるため、それらの情報を参考にして最適なアクションを選択してください。

## Slack以外の通知や操作に関するアクション

GitHub Actionsでは、多岐にわたる通知や操作を行うためのアクションが提供されています。以下はその中の一部の例です：

1. **[Email Notification Action](https://github.com/marketplace/actions/email-notification-action)**
   - **目的**: ワークフローの結果をメールで通知するためのアクションです。
   - **特徴**: ジョブの成功や失敗に応じて、異なるメッセージや件名を設定することができます。また、複数の受信者に対して通知を送ることも可能です。

2. **[OneLogin Actions](https://github.com/marketplace/actions/onelogin-actions)**
   - **目的**: OneLoginのアカウントや設定に対して操作を行うためのアクションです。
   - **特徴**: アカウントの作成や削除、パスワードのリセットなど、OneLoginに関する様々な操作をワークフローの中で自動的に実行することができます。

3. **[Google Cloud Actions]([https://github.com/marketplace/actions/google-cloud-platform-gcp-actions](https://github.com/google-github-actions))**
   - **目的**: Google Cloud Platformのサービスやリソースに対して操作を行うためのアクションです。
   - **特徴**: Google Cloud Storageのバケットの作成や削除、Google Kubernetes Engineのクラスタのデプロイなど、GCPに関する多岐にわたる操作をサポートしています。

4. **[SMS Notification](https://github.com/marketplace/actions/sms-notification-action)**
   - **目的**: ワークフローの結果をSMSで通知するためのアクションです。
   - **特徴**: 重要なジョブの結果をリアルタイムで知ることができるため、緊急の対応が必要な場合などに役立ちます。

これらのアクションを使用することで、様々な方法でGitHub Actionsのワークフローの結果を通知することができます。また、特定のサービスやプラットフォームに対する操作を自動化することも可能です。プロジェクトの要件や通知の目的に応じて、最適なアクションを選択してください。
