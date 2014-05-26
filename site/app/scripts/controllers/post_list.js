'use strict';

angular.module('siteApp')
  .controller('PostListCtrl', [
    '$scope', 'FileRetriever',
    function ($scope, FileRetriever) {
      function init() {
        FileRetriever.fetch('title').then(function(posts) {
          $scope.posts = posts;
        });
      }

      init();
    }
  ]);
