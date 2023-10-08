
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
3. ワークフローファイルを以下のように編集します:

\```yaml
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
\```

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

