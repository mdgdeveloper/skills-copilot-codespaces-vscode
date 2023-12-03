// Create web server
const express = require('express');
const router = express.Router();
const Comment = require('../models/comment');
const Post = require('../models/post');
const User = require('../models/user');

