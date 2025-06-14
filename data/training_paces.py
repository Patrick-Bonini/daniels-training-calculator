TRAINING_PACES = {
    'VDOT': list(range(30, 86)),
    'E/L km': ['7:27-8:14', '7:16-8:02', '7:05-7:52', '6:55-7:41', '6:45-7:31', '6:36-7:21',
               '6:27-7:11', '6:19-7:02', '6:11-6:54', '6:03-6:46', '5:56-6:38', '5:49-6:31',
               '5:42-6:23', '5:35-6:16', '5:29-6:10', '5:23-6:03', '5:17-5:57', '5:12-5:51',
               '5:07-5:45', '5:01-5:40', '4:56-5:34', '4:52-5:29', '4:47-5:24', '4:43-5:19',
               '4:38-5:14', '4:34-5:10', '4:30-5:05', '4:26-5:01', '4:22-4:57', '4:19-4:53',
               '4:15-4:49', '4:11-4:45', '4:08-4:41', '4:04-4:37', '4:00-4:33', '3:57-4:30',
               '3:54-4:26', '3:51-4:23', '3:48-4:19', '3:45-4:16', '3:42-4:13', '3:39-4:10',
               '3:36-4:07', '3:34-4:04', '3:31-4:01', '3:28-3:58', '3:26-3:55', '3:23-3:52',
               '3:21-3:49', '3:18-3:46', '3:16-3:44', '3:13-3:41', '3:11-3:38', '3:09-3:36',
               '3:07-3:34', '3:05-3:32'],
    'E/L mile': ['12:00-13:16', '11:41-12:57', '11:24-12:39', '11:07-12:21', '10:52-12:05', '10:37-11:49',
                 '10:23-11:34', '10:09-11:20', '9:56-11:06', '9:44-10:53', '9:32-10:41', '9:21-10:28',
                 '9:10-10:17', '9:00-10:05', '8:59-9:55', '8:04-9:44', '8:31-9:34', '8:22-9:25',
                 '8:13-9:15', '8:05-9:06', '7:57-8:58', '7:49-8:49', '7:42-8:41', '7:35-8:33',
                 '7:28-8:26', '7:21-8:18', '7:15-8:11', '7:08-8:04', '7:02-7:58', '6:56-7:51',
                 '6:50-7:45', '6:45-7:39', '6:39-7:33', '6:34-7:27', '6:29-7:21', '6:24-7:15',
                 '6:19-7:09', '6:14-7:03', '6:09-6:57', '6:04-6:51', '5:59-6:45', '5:54-6:39',
                 '5:49-6:33', '5:45-6:27', '5:40-6:21', '5:36-6:15', '5:32-6:09', '5:28-6:03',
                 '5:24-5:57', '5:20-5:51', '5:16-5:45', '5:12-5:39', '5:08-5:33', '5:04-5:27',
                 '5:00-5:21', '4:56-5:15'],
    'M km': ['7:03', '6:52', '6:40', '6:30', '6:20', '6:10', '6:01', '5:53', '5:45', '5:37',
             '5:29', '5:22', '5:16', '5:09', '5:03', '4:57', '4:51', '4:46', '4:41', '4:36',
             '4:31', '4:27', '4:22', '4:18', '4:14', '4:10', '4:06', '4:03', '3:59', '3:56',
             '3:52', '3:49', '3:46', '3:43', '3:40', '3:37', '3:34', '3:31', '3:28', '3:25',
             '3:22', '3:19', '3:16', '3:14', '3:11', '3:08', '3:06', '3:04', '3:01', '2:59',
             '2:57', '2:55', '2:53', '2:51', '2:49', '2:47'],
    'M mile': ['11:21', '11:02', '10:44', '10:27', '10:11', '9:56', '9:41', '9:28', '9:15', '9:02',
               '8:50', '8:39', '8:28', '8:17', '8:07', '7:58', '7:49', '7:40', '7:32', '7:24',
               '7:17', '7:09', '7:02', '6:56', '6:49', '6:43', '6:37', '6:31', '6:25', '6:19',
               '6:14', '6:09', '6:04', '5:59', '5:54', '5:50', '5:45', '5:41', '5:37', '5:33',
               '5:29', '5:25', '5:21', '5:17', '5:13', '5:09', '5:06', '5:02', '4:59', '4:55',
               '4:52', '4:48', '4:45', '4:42', '4:39', '4:36'],
    'T km': ['6:24', '6:14', '6:05', '5:56', '5:48', '5:40', '5:33', '5:26', '5:19', '5:12',
             '5:06', '5:00', '4:54', '4:49', '4:43', '4:38', '4:33', '4:29', '4:24', '4:20',
             '4:15', '4:11', '4:07', '4:04', '4:00', '3:56', '3:53', '3:50', '3:46', '3:43',
             '3:40', '3:37', '3:34', '3:31', '3:28', '3:25', '3:22', '3:19', '3:16', '3:14',
             '3:11', '3:08', '3:06', '3:04', '3:01', '2:59', '2:57', '2:55', '2:53', '2:51',
             '2:49', '2:47', '2:45', '2:43', '2:41', '2:39'],
    'T mile': ['10:18', '10:02', '9:47', '9:33', '9:20', '9:07', '8:55', '8:44', '8:33', '8:22',
               '8:12', '8:02', '7:52', '7:42', '7:33', '7:25', '7:17', '7:09', '7:02', '6:56',
               '6:50', '6:44', '6:38', '6:32', '6:26', '6:20', '6:15', '6:09', '6:04', '5:59',
               '5:54', '5:50', '5:45', '5:41', '5:37', '5:33', '5:29', '5:25', '5:21', '5:17',
               '5:13', '5:09', '5:06', '5:02', '4:59', '4:55', '4:52', '4:48', '4:45', '4:42',
               '4:39', '4:36', '4:33', '4:30', '4:27', '4:24'],
    'I 400m': ['2:22', '2:18', '2:14', '2:11', '2:08', '2:05', '2:02', '1:59', '1:56', '1:54',
               '1:52', '1:50', '1:48', '1:46', '1:44', '1:42', '1:40', '1:38', '1:36', '1:35',
               '1:33', '1:31', '1:30', '1:29', '1:28', '1:27', '1:26', '1:25', '1:24', '1:23',
               '1:22', '1:21', '1:20', '1:19', '1:18', '1:17', '1:16', '1:15', '1:14', '1:13',
               '1:12', '1:11', '1:10', '1:09', '1:08', '1:07', '1:06', '1:05', '1:04', '1:03',
               '1:02', '1:01', '1:00', '0:59', '0:58', '0:57'],
    'I km': ['—', '—', '—', '—', '—', '—', '—', '5:00', '4:54', '4:48', '4:42', '4:36', '4:31',
             '4:26', '4:21', '4:16', '4:12', '4:07', '4:03', '3:59', '3:55', '3:51', '3:48',
             '3:44', '3:41', '3:37', '3:34', '3:31', '3:28', '3:25', '3:23', '3:20', '3:17',
             '3:14', '3:12', '3:09', '3:07', '3:04', '3:02', '3:00', '2:57', '2:55', '2:53',
             '2:51', '2:49', '2:47', '2:45', '2:43', '2:41', '2:39', '2:37', '2:35', '2:33',
             '2:31', '2:29', '2:27'],
    'I 1200m': ['—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—',
                '5:00', '4:54', '4:49', '4:45', '4:40', '4:36', '4:32', '4:29', '4:25', '4:21',
                '4:18', '4:14', '4:10', '4:07', '4:03', '4:00', '3:57', '3:54', '3:51', '3:48',
                '3:45', '3:42', '3:39', '3:36', '3:34', '3:31', '3:29', '3:26', '3:24', '3:21',
                '3:19', '3:17', '3:15', '3:13', '3:11', '3:09', '3:07', '3:05', '3:03', '3:01'],
    'I mile': ['—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—',
               '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—',
               '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—',
               '—', '—', '—', '—', '—', '—', '—', '—'],
    'R 200m': ['67', '65', '63', '61', '60', '58', '57', '55', '54', '53', '52', '51', '50',
               '49', '48', '47', '46', '45', '44', '44', '43', '43', '42', '42', '41', '40',
               '40', '39', '38', '38', '37', '37', '37', '36', '36', '35', '35', '34', '34',
               '33', '33', '32', '32', '31', '31', '30', '30', '30', '29', '29', '29', '28',
               '28', '28', '27', '27'],
    'R 300m': ['141', '98', '95', '92', '90', '87', '85', '83', '81', '80', '78', '77', '75',
               '74', '72', '71', '69', '68', '67', '66', '65', '64', '64', '63', '62', '61',
               '60', '59', '58', '57', '56', '55', '55', '54', '53', '52', '52', '51', '50',
               '50', '49', '49', '48', '48', '47', '47', '46', '46', '45', '45', '44', '44',
               '43', '43', '42', '42'],
    'R 400m': ['—', '—', '—', '—', '200', '157', '154', '151', '148', '146', '144', '142', '140',
               '98', '96', '94', '92', '90', '89', '88', '87', '86', '85', '84', '82', '81',
               '80', '79', '77', '76', '75', '74', '74', '73', '72', '71', '70', '69', '68',
               '67', '67', '66', '65', '64', '64', '63', '62', '62', '61', '60', '60', '59',
               '59', '58', '58', '57'],
    'R 600m': ['—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—',
               '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '200', '157', '154', '152',
               '151', '150', '148', '147', '145', '144', '142', '141', '140', '138', '137', '136',
               '135', '134', '133', '132', '131', '130', '129', '128', '127', '126', '125', '124',
               '123'],
    'R 800m': ['—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—',
               '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '200', '157', '155', '154',
               '152', '151', '150', '148', '147', '145', '144', '142', '141', '140', '138', '137',
               '136', '135', '134', '133', '132', '131', '130', '129', '128', '127', '126', '125',
               '124', '123']
}