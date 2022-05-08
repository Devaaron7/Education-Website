<?php

$targetPath = "for_teacher/" . basename($_FILES["pdf"]["name"]);
move_uploaded_file($_FILES["pdf"]["tmp_name"], $targetPath);


?>