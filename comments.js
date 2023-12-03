// Create a web server

const express = require('express');
const router = express.Router();

const Comment = require('../models/comment');

// POST /comments
// Create a new comment
router.post('/', function(req, res, next) {
  const comment = new Comment({
    name: req.body.name,
    email: req.body.email,
    message: req.body.message,
    timestamp: Date.now()
  });

  comment.save(function(err, comment) {
    if (err) {
      return next(err);
    }
    res.status(201);
    res.json(comment);
  });
});

// GET /comments
// Get a list of comments
router.get('/', function(req, res, next) {
  Comment.find({}, function(err, comments) {
    if (err) {
      return next(err);
    }
    res.json(comments);
  });
});

// GET /comments/:id
// Get a single comment
router.get('/:id', function(req, res, next) {
  Comment.findById(req.params.id, function(err, comment) {
    if (err) {
      return next(err);
    }
    if (!comment) {
      return res.status(404).json({
        message: 'Comment not found'
      });
    }
    res.json(comment);
  });
});

// DELETE /comments/:id
// Delete a comment
router.delete('/:id', function(req, res, next) {
  Comment.findByIdAndRemove(req.params.id, function(err, comment) {
    if (err) {
      return next(err);
    }
    if (!comment) {
      return res.status(404).json({
        message: 'Comment not found'
      });
    }
    res.json(comment);
  });
});

module.exports = router;