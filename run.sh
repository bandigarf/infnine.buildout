#!/bin/bash

DIR=$(dirname $0)
$DIR/bin/zeo start
$DIR/bin/zope-primary start
