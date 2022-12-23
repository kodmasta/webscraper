#include <iostream>
#include "nlohmann/json.hpp"
#include <string>
#include <cstring>
#include <fstream>

using json = nlohmann::json;
using namespace std;


bool isClickBait(string title)
{
    double prob = 0;

    if (title.find("没") != string::npos)
        prob = prob + 0.30;
    if (title.find("险") != string::npos)
        prob = prob + 0.30;
    if (title.find("惊") != string::npos)
        prob = prob + 0.30;
    if (title.find("呆") != string::npos)
        prob = prob + 0.30;
    if (title.find("震") != string::npos)
        prob = prob + 0.30;
    if (title.find("撼") != string::npos)
        prob = prob + 0.30;
    if (title.find("吓") != string::npos)
        prob = prob + 0.30;
    if (title.find("傻") != string::npos)
        prob = prob + 0.30;
    if (title.find("骗") != string::npos)
        prob = prob + 0.30;
    if (title.find("爆") != string::npos)
        prob = prob + 0.30;
    if (title.find("财富") != string::npos)
        prob = prob + 0.30;
    if (title.find("密码") != string::npos)
        prob = prob + 0.30;
    if (title.find("译局") != string::npos)
        prob = prob + 0.30;
    if (title.find("破") != string::npos)
        prob = prob + 0.30;
    if (title.find("打") != string::npos)
        prob = prob + 0.30;
    if (title.find("千万") != string::npos)
        prob = prob + 0.30;
    if (title.find("罚") != string::npos)
        prob = prob + 0.30;
    if (title.find("谨记") != string::npos)
        prob = prob + 0.30;
    if (title.find("不") != string::npos)
        prob = prob + 0.30;
    if (title.find("了") != string::npos)
        prob = prob + 0.30;
    if (title.find("香") != string::npos)
        prob = prob + 0.30;
    if (title.find("吃") != string::npos)
        prob = prob + 0.30;
    if (title.find("定") != string::npos)
        prob = prob + 0.30;
    if (title.find("好") != string::npos)
        prob = prob + 0.30;
    if (title.find("严") != string::npos)
        prob = prob + 0.30;
    if (title.find("极") != string::npos)
        prob = prob + 0.30;
    if (title.find("端") != string::npos)
        prob = prob + 0.30;
    if (title.find("拒") != string::npos)
        prob = prob + 0.30;
    if (title.find("绝") != string::npos)
        prob = prob + 0.30;
    if (title.find("巨") != string::npos)
        prob = prob + 0.30;
    if (title.find("大") != string::npos)
        prob = prob + 0.30;
    if (title.find("快") != string::npos)
        prob = prob + 0.30;
    if (title.find("看") != string::npos)
        prob = prob + 0.30;
    if (title.find("坏") != string::npos)
        prob = prob + 0.30;
    if (title.find("偷") != string::npos)
        prob = prob + 0.30;
    if (title.find("逃") != string::npos)
        prob = prob + 0.30;

    if (title.find("!") != string::npos)
        prob = prob + 0.60;
    if (title.find("！") != string::npos)
        prob = prob + 0.60;
    if (title.find("?") != string::npos)
        prob = prob + 0.60;
    if (title.find("？") != string::npos)
        prob = prob + 0.60;
    if (title.find("。。。") != string::npos)
        prob = prob + 0.60;
    if (title.find("...") != string::npos)
        prob = prob + 0.60;
    if (title.find("危") != string::npos)
        prob = prob + 0.60;
    if (title.find("天呀") != string::npos)
        prob = prob + 0.60;
    if (title.find("一口气") != string::npos)
        prob = prob + 0.60;
    if (title.find("秘密") != string::npos)
        prob = prob + 0.60;
    if (title.find("暴跌") != string::npos)
        prob = prob + 0.60;
    if (title.find("暴涨") != string::npos)
        prob = prob + 0.60;
    if (title.find("骗局") != string::npos)
        prob = prob + 0.60;
    if (title.find("居然") != string::npos)
        prob = prob + 0.60;
    if (title.find("切记") != string::npos)
        prob = prob + 0.60;
    if (title.find("解密") != string::npos)
        prob = prob + 0.60;
    if (title.find("揭秘") != string::npos)
        prob = prob + 0.60;
    if (title.find("慌") != string::npos)
        prob = prob + 0.60;
    if (title.find("注意") != string::npos)
        prob = prob + 0.60;
    if (title.find("小心") != string::npos)
        prob = prob + 0.60;
    if (title.find("警告") != string::npos)
        prob = prob + 0.60;
    if (title.find("亿") != string::npos)
        prob = prob + 0.60;
    if (title.find("万") != string::npos)
        prob = prob + 0.60;
    if (title.find("万") != string::npos)
        prob = prob + 0.30;
    if (title.find("发现") != string::npos)
        prob = prob + 0.30;
    
    if (prob >= 0.6)
        return true;
    else
        return false;
}

int main(int argc, const char * argv[])
{
    json j;
    ifstream i("caijing_clickbait_titles.json");
    i >> j;
//    for (auto it = j.begin(); it != j.end(); ++it)
//    {
//        cout << (*it)["title"] << endl;
//        if(!isClickBait((*it)["title"]))
//        {
//            j.erase(it);
//            --it;
//        }
//        
//    }
    int count = 0;
    for (auto it = j.begin(); it != j.end(); ++it)
    {
        string temp = (*it)["title"];
        temp.erase(0,7);
        cout <<temp << endl;
        (*it)["title"] = temp;
    }
    ofstream o("caijing_clickbait_titles2.json");
        o << std::setw(4) << j << std::endl;
    
    return 0;
}
