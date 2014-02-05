'use strict';

angular.module('siteApp')
  .service('FileRetriever', [
    '$http', '$q',
    function FileRetriever($http, $q) {
      this.fetch = function(path) {
        var delay = $q.defer();
        $http.get('/index/' + path)
          .success(function(data, status, headers, config) {
            delay.resolve(data)
          })
          .error(function(data, status, headers, config) {
            delay.reject('Unable to fetch the file');
          })
        return delay.promise;
      }
    }
  ]);
