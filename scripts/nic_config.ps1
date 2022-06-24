netsh interface ip set address $args[0] static $args[1] $args[2] $args[3] | out-null
netsh interface ip set dns $args[0] static $args[4] | out-null
return $?