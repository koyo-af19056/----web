<!DOCTYPE html>

<head>
    <title>地方創生webサイト</title>
    <link rel='stylesheet' href='<?php echo get_template_directory_uri(); ?>/mystyle.css' type='text/css'>
</head>

<body>
    <header>
        <div id="title_label">
            <div class="title">
                <a>my first edition</a>
            </div>
            <div class="header_menu_label">
                <div class="header_menu">
                    <a href='<?php echo home_url('/municipality'); ?>'>自治体情報</a>
                </div>
                <div class="header_menu">
                    <a>イベント情報</a>
                </div>
                <div class="header_menu">
                    <a>日本地図クイズ</a>
                </div>

                <div class="header_menu">
                    <a>お問い合わせ</a>
                </div>
            </div>
            <div id="humberger">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    </header>