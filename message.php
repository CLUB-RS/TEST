<?php

require 'vendor/message.php';

use danog\MadelineProto\API;
use danog\MadelineProto\EventHandler;

class MyEventHandler extends EventHandler
{
    public function onAny($update)
    {
        // Handle different types of updates
        if (isset($update['message'])) {
            $this->onMessage($update['message']);
        }
    }

    public function onMessage($message)
    {
        $user_id = $message['from']['id'];
        $text = "Sender ID: $user_id\nMessage: {$message['text']}";

        // Replace 'YOUR_GROUP_ID' with your actual group ID
        $this->messages->sendMessage(['peer' => 'YOUR_GROUP_ID', 'message' => $text]);

        // Reply to the user
        $this->messages->sendMessage(['peer' => $user_id, 'message' => "Your message has been received and forwarded!"]);
    }
}

$settings = [
    'app_info' => [
        'api_id' => 'your_api_id',
        'api_hash' => 'your_api_hash',
    ],
];

$MadelineProto = new API('session.madeline', $settings);
$MadelineProto->start();

$MadelineProto->setEventHandler(MyEventHandler::class);
$MadelineProto->loop(-1);

?>
