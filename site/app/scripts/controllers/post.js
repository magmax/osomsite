'use strict';

angular.module('siteApp')
  .controller('PostCtrl', [
    function ($scope) {
    '$scope', '$routeParams', 'FileRetriever',
    function ($scope, $routeParams, FileRetriever) {
      function init() {
        FileRetriever.fetch('/post/' + $routeParams.filename).then(function(post) {
          $scope.html = post;
        });
      }

      init();
    }
    }
  ]);
