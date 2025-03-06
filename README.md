# 中国政府网站数据爬虫 (Crawler of China Government Websites)

[English Version](#english-version)

## 中文版本

### 项目简介
该项目是一个用于爬取中国大陆政府官方网站数据的爬虫系统，主要关注政府公告、新闻和其他相关信息。系统支持全国所有省级行政区（包括直辖市、自治区）以及地级市的政府网站数据采集。本项目采用模块化设计，支持灵活配置和扩展，确保数据采集的准确性和效率。

### 主要功能
- 多级政府网站数据采集
  - 支持省级、地级市政府网站数据爬取
  - 支持多省份、多城市并发爬取
  - 自动处理自治区特殊命名规则
- 数据处理能力
  - 支持多种数据获取方式（API、网页解析）
  - 数据自动清洗和标准化
  - 智能处理各地区政府网站差异
- 数据存储与导出
  - 结果保存为标准Excel格式
  - 支持按时间范围分类存储
  - 支持按地区分类管理数据

### 支持的地区
#### 省级行政区
- 直辖市：北京市、天津市、上海市、重庆市
- 省份：河北省、山西省、辽宁省、吉林省、黑龙江省、江苏省、浙江省、安徽省、福建省、江西省、山东省、河南省、湖北省、湖南省、广东省、海南省、四川省、贵州省、云南省、陕西省、甘肃省、青海省
- 自治区：内蒙古自治区、广西壮族自治区、西藏自治区、宁夏回族自治区、新疆维吾尔自治区

### 项目结构
```
Crawler_of_China_govern_website/
│
├── .idea/                          # IDE配置文件
├── output/                         # 输出数据目录
│     ├── Total_time_range_data/   # 全部地级市的全部时间段数据
│     ├── Certain_time_range_data/ # 特定地级市的特定时间段数据
│     └── province_web_src/        # 各省份和直辖市的政府网站数据
│     
├── src/                           # 源代码目录
│     ├── spider/                  # 爬虫核心实现
│     │     ├── base_spider.py     # 爬虫基类
│     │     └── utils.py          # 爬虫工具类
│     ├── common/                  # 通用工具类
│     │     ├── config.py         # 配置文件
│     │     └── utils.py          # 通用工具函数
│     ├── analysis/               # 数据分析模块
│     ├── certain_city_src/       # 特定地级市爬虫
│     ├── province_web_src/       # 省级网站爬虫
│     ├── total_city_src/         # 全部地级市爬虫
│     └── requirements.txt        # 项目依赖
├── .gitignore                    # Git忽略文件
├── LICENSE                       # 开源协议
└── README.md                     # 项目说明文档
```

### 技术栈
- Python 3.8+
- 核心依赖：
  - DrissionPage：网页抓取
  - pandas：数据处理
  - requests：HTTP请求
  - concurrent.futures：并发处理
  - loguru：日志记录

### 安装和使用
1. 克隆项目
```bash
git clone https://github.com/YourUsername/Crawler_of_China_govern_website.git
cd Crawler_of_China_govern_website
```

2. 创建并激活虚拟环境（推荐）
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 配置爬虫参数
在`src/spider/config.py`中配置相关参数：
```python
CRAWLER_CONFIG = {
    'max_retries': 3,           # 最大重试次数
    'timeout': 30,              # 请求超时时间
    'concurrent_threads': 5,    # 并发线程数
    'delay': 1,                # 请求间隔（秒）
}
```

5. 运行爬虫
```bash
# 爬取特定城市数据
python src/certain_city_src/main.py

# 爬取省级网站数据
python src/province_web_src/main.py

# 爬取所有城市数据
python src/total_city_src/main.py
```

### 数据格式
爬取的数据将保存为Excel文件，包含以下字段：
- code：城市编码
- province：省份名称
- city：城市名称
- topic：新闻标题
- date：发布日期
- url：新闻链接
- content：新闻内容
- source：信息来源
- category：新闻类别
- update_time：数据更新时间

### 注意事项
1. 爬虫使用规范
   - 请遵守网站的robots.txt规则
   - 建议设置适当的爬取间隔，避免对目标网站造成压力
   - 部分网站可能需要配置代理IP
   
2. 数据处理
   - 定期检查数据完整性
   - 建议对重要数据进行备份
   - 注意处理特殊字符和编码问题

3. 系统要求
   - 推荐使用Windows 10或Linux操作系统
   - 确保有足够的磁盘空间存储数据
   - 建议内存8GB以上

### 常见问题解决
1. 连接超时
   - 检查网络连接
   - 适当增加超时时间
   - 考虑使用代理IP

2. 数据解析错误
   - 检查网页结构是否变化
   - 更新解析规则
   - 查看日志获取详细错误信息

### 贡献指南
欢迎贡献代码，请遵循以下步骤：
1. Fork 项目
2. 创建新的分支
3. 提交更改
4. 发起 Pull Request

### 许可证
MIT License

### 联系方式
- 项目维护者：[维护者姓名]
- 邮箱：[联系邮箱]
- GitHub：[GitHub主页]

---

## English Version

### Project Overview
This project is a comprehensive web crawler system designed to collect data from official government websites in mainland China. It focuses on government announcements, news, and other related information. The system supports data collection from all provincial-level administrative regions (including municipalities and autonomous regions) and prefecture-level cities.

### Key Features
- Multi-level Government Website Data Collection
  - Support for provincial and city-level government websites
  - Multi-province and multi-city concurrent crawling
  - Automatic handling of autonomous region naming
- Data Processing Capabilities
  - Multiple data acquisition methods (API, webpage parsing)
  - Automatic data cleaning and standardization
  - Intelligent handling of regional website differences
- Data Storage and Export
  - Results saved in standard Excel format
  - Time-range based storage support
  - Regional data classification management

### Supported Regions
#### Provincial Administrative Regions
- Municipalities: Beijing, Tianjin, Shanghai, Chongqing
- Provinces: Hebei, Shanxi, Liaoning, Jilin, Heilongjiang, Jiangsu, Zhejiang, Anhui, Fujian, Jiangxi, Shandong, Henan, Hubei, Hunan, Guangdong, Hainan, Sichuan, Guizhou, Yunnan, Shaanxi, Gansu, Qinghai
- Autonomous Regions: Inner Mongolia, Guangxi, Tibet, Ningxia, Xinjiang

### Project Structure
```
Crawler_of_China_govern_website/
│
├── .idea/                          # IDE configuration files
├── output/                         # Output data directory
│     ├── Total_time_range_data/   # All cities' data across time
│     ├── Certain_time_range_data/ # Specific cities' data for specific periods
│     └── province_web_src/        # Provincial and municipal government website data
│     
├── src/                           # Source code directory
│     ├── spider/                  # Core crawler implementation
│     │     ├── base_spider.py     # Base crawler class
│     │     └── utils.py          # Crawler utilities
│     ├── common/                  # Common utilities
│     │     ├── config.py         # Configuration file
│     │     └── utils.py          # Common utility functions
│     ├── analysis/               # Data analysis module
│     ├── certain_city_src/       # Specific city crawlers
│     ├── province_web_src/       # Provincial website crawlers
│     ├── total_city_src/         # All-city crawlers
│     └── requirements.txt        # Project dependencies
├── .gitignore                    # Git ignore file
├── LICENSE                       # License file
└── README.md                     # Project documentation
```

### Tech Stack
- Python 3.8+
- Core Dependencies:
  - DrissionPage: Web scraping
  - pandas: Data processing
  - requests: HTTP requests
  - concurrent.futures: Concurrent processing
  - loguru: Logging

### Installation and Usage
1. Clone the project
```bash
git clone https://github.com/YourUsername/Crawler_of_China_govern_website.git
cd Crawler_of_China_govern_website
```

2. Create and activate virtual environment (recommended)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure crawler parameters
In `src/spider/config.py`:
```python
CRAWLER_CONFIG = {
    'max_retries': 3,           # Maximum retry attempts
    'timeout': 30,              # Request timeout
    'concurrent_threads': 5,    # Number of concurrent threads
    'delay': 1,                # Request delay (seconds)
}
```

5. Run the crawler
```bash
# Crawl specific city data
python src/certain_city_src/main.py

# Crawl provincial website data
python src/province_web_src/main.py

# Crawl all city data
python src/total_city_src/main.py
```

### Data Format
The crawled data will be saved as Excel files with the following fields:
- code: City code
- province: Province name
- city: City name
- topic: News title
- date: Publication date
- url: News link
- content: News content
- source: Information source
- category: News category
- update_time: Data update time

### Important Notes
1. Crawler Usage Guidelines
   - Comply with website robots.txt rules
   - Set appropriate crawling intervals
   - Configure proxy IPs when necessary
   
2. Data Processing
   - Regular data integrity checks
   - Backup important data
   - Handle special characters and encoding issues

3. System Requirements
   - Recommended: Windows 10 or Linux
   - Sufficient disk space for data storage
   - Recommended: 8GB+ RAM

### Troubleshooting
1. Connection Timeouts
   - Check network connection
   - Increase timeout duration
   - Consider using proxy IPs

2. Data Parsing Errors
   - Check for website structure changes
   - Update parsing rules
   - Review logs for detailed error information

### Contributing
Contributions are welcome! Please follow these steps:
1. Fork the project
2. Create a new branch
3. Submit changes
4. Create a Pull Request

### License
MIT License

### Contact
- Maintainer: [Maintainer Name]
- Email: [Contact Email]
- GitHub: [GitHub Profile]
