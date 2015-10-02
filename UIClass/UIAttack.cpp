//
//  UIAttack.cpp
//  game4
//
//  Created by Junpeng Zhang on 2/3/15.
//  本代码由工具生成
//资源加载适合cocos2d-x 3.2版本的cocostuido 1.6 for windows
//

#include "UIAttack.h"
#include "strHash.h"
////
////  strHash.h
////  game1
////  使用结构体来进行游戏属性存储会比较方便快捷
//// C++11新特性
////  Created by 俊盟科技1 on 8/26/14.
////
////
////为了使用字符串作为switch的case分支，这里加了些方法
//
//#ifndef game1_strHash_h
//#define game1_strHash_h
//#include "cocos2d.h"
//using namespace std;
//
//typedef std::uint64_t hash_t;
//
//constexpr hash_t prime = 0x100000001B3ull;
//constexpr hash_t basis = 0xCBF29CE484222325ull;
//
//hash_t hash_(char const* str);
////{
////    hash_t ret{basis};
////    
////    while(*str){
////        ret ^= *str;
////        ret *= prime;
////        str++;
////    }
////    
////    return ret;
////}
//
//constexpr hash_t hash_compile_time(char const* str, hash_t last_value = basis)
//{
//    return *str ? hash_compile_time(str+1, (*str ^ last_value) * prime) : last_value;
//}
//
//constexpr unsigned long long operator "" _hash(char const* p, size_t)
//{
//    return hash_compile_time(p);
//}
//
///*字符串作为case例子
//void simple_switch(char const* str)
//{
//    using namespace std;
//    switch(hash_(str)){
//        case "first"_hash:
//            cout << "1st one" << endl;
//            break;
//        case "second"_hash:
//            cout << "2nd one" << endl;
//            break;
//        case "third"_hash:
//            cout << "3rd one" << endl;
//            break;
//        default:
//            cout << "Default..." << endl;
//    }
//}
// */

#define kSoundButton "sound/Click_Button.wav"

USING_NS_CC;
using namespace ui;
using namespace std;
UIAttack::UIAttack()
{
    
}
UIAttack::~UIAttack()
{
    
}
cocos2d::Ref* UIAttack::getUIConfData()
{
    __String* str = __String::createWithFormat("%d",m_uiID);
    return str;
}
UIAttack* UIAttack::createFromManger(Ref* dat)
{
    UIAttack* tmp = new UIAttack();
    if(tmp){
        tmp->autorelease();
        __String* st = dynamic_cast<__String*>(dat);
        tmp->m_uiID = st->intValue();
        tmp->m_uiName = "UIAttack";
        tmp->init();
        return tmp;
    }else{
        return nullptr;
    }
}
UIAttack* UIAttack::create(int uiID)
{
    UIAttack* tmp = new UIAttack();
    if(tmp){
        tmp->autorelease();
        tmp->m_uiID = uiID;
        tmp->m_uiName = "UIAttack";
        tmp->init();
        return tmp;
    }else{
        return nullptr;
    }
}
UIAttack* UIAttack::create()
{
    UIAttack* tmp = new UIAttack();
    if(tmp){
        tmp->autorelease();
        tmp->m_uiName = "UIAttack";
        tmp->init();
        return tmp;
    }else{
        return nullptr;
    }
    
}
// on "init" you need to initialize your instance
bool UIAttack::init()
{
    //////////////////////////////
    // 1. super init first
    if ( !Layer::init() )
    {
        return false;
    }

    SpriteFrameCache::getInstance()->addSpriteFramesWithFile(uiplist/UIAttack0.plist);
    m_rootLayout = dynamic_cast<ui::Layout*>(GUIReader::getInstance()->widgetFromJsonFile("ui//UIAttack.ExportJson"));
    //Button
    m_btn_leftBtn = dynamic_cast<ui::Button*>(Helper::seekWidgetByName(m_rootLayout, "btn_left"));
    m_btn_leftBtn->addTouchEventListener(CC_CALLBACK_2(UIAttack::onTouchEvent, this));
    m_btn_rightBtn = dynamic_cast<ui::Button*>(Helper::seekWidgetByName(m_rootLayout, "btn_right"));
    m_btn_rightBtn->addTouchEventListener(CC_CALLBACK_2(UIAttack::onTouchEvent, this));
    m_btn_buyBtn = dynamic_cast<ui::Button*>(Helper::seekWidgetByName(m_rootLayout, "btn_buy"));
    m_btn_buyBtn->addTouchEventListener(CC_CALLBACK_2(UIAttack::onTouchEvent, this));
    m_btn_backBtn = dynamic_cast<ui::Button*>(Helper::seekWidgetByName(m_rootLayout, "btn_back"));
    m_btn_backBtn->addTouchEventListener(CC_CALLBACK_2(UIAttack::onTouchEvent, this));

    //ImageView
    m_img_uiattackBGImage = dynamic_cast<ImageView*>(Helper::seekWidgetByName(m_rootLayout, "img_uiattackBG"));
    m_img_frambgImage = dynamic_cast<ImageView*>(Helper::seekWidgetByName(m_rootLayout, "img_frambg"));
    m_img_tablebgImage = dynamic_cast<ImageView*>(Helper::seekWidgetByName(m_rootLayout, "img_tablebg"));
    m_img_mainbgImage = dynamic_cast<ImageView*>(Helper::seekWidgetByName(m_rootLayout, "img_mainbg"));
    Widget* tmpximg_mainbg = Helper::seekWidgetByName(m_rootLayout, "img_mainbg");
    ImageView* p_image4 = dynamic_cast<ui::ImageView*>(Helper::seekWidgetByName(tmpximg_mainbg, "img_sel"));
    m_img_assistantbgImage = dynamic_cast<ImageView*>(Helper::seekWidgetByName(m_rootLayout, "img_assistantbg"));
    Widget* tmpximg_assistantbg = Helper::seekWidgetByName(m_rootLayout, "img_assistantbg");
    ImageView* p_image6 = dynamic_cast<ui::ImageView*>(Helper::seekWidgetByName(tmpximg_assistantbg, "img_sel"));
    m_img_skillBGImage = dynamic_cast<ImageView*>(Helper::seekWidgetByName(m_rootLayout, "img_skillBG"));
    Widget* tmpxlay_skillPanel = Helper::seekWidgetByName(m_rootLayout, "lay_skillPanel");
    ImageView* p_image8 = dynamic_cast<ui::ImageView*>(Helper::seekWidgetByName(tmpxlay_skillPanel, "img_skill1"));
    Widget* tmpxlay_skillPanel = Helper::seekWidgetByName(m_rootLayout, "lay_skillPanel");
    ImageView* p_image9 = dynamic_cast<ui::ImageView*>(Helper::seekWidgetByName(tmpxlay_skillPanel, "img_skill2"));
    Widget* tmpxlay_skillPanel = Helper::seekWidgetByName(m_rootLayout, "lay_skillPanel");
    ImageView* p_image10 = dynamic_cast<ui::ImageView*>(Helper::seekWidgetByName(tmpxlay_skillPanel, "img_skill3"));
    m_img_txt_mainImage = dynamic_cast<ImageView*>(Helper::seekWidgetByName(m_rootLayout, "img_txt_main"));
    m_img_txt_assImage = dynamic_cast<ImageView*>(Helper::seekWidgetByName(m_rootLayout, "img_txt_ass"));
    //Panel
    m_lay_skillPanelLayout = dynamic_cast<Layout*>(Helper::seekWidgetByName(m_rootLayout, "lay_skillPanel"));
    this->initLayoutlay_skillPanel();


    this->addChild(m_rootLayout);
    return true;
}

void UIAttack::close()
{
    this->removeFromParent();
}
//buttonEvent

void UIAttack::onTouchEvent(cocos2d::Ref *pSender, Widget::TouchEventType type)
{
    //按下、移动、结束、取消
   // string buttonname = btntmp->getName();
    switch (type)
    {
        case Widget::TouchEventType::ENDED:
        {
            this->onWidgetTouchEnd(pSender);
        }
            break;
        case Widget::TouchEventType::BEGAN:
        {
            this->onWidgetTouchBeigen(pSender);
        }
            break;
        case Widget::TouchEventType::MOVED:
        {
            this->onWidgetTouchMove(pSender);
        }
            break;
        case Widget::TouchEventType::CANCELED:
        {
            this->onWidgetTouchCanceled(pSender);
        }
            break;
        default:
            break;
    }

}

void UIAttack::onWidgetTouchBeigen(cocos2d::Ref *pSender)
{
    Widget* btntmp = dynamic_cast<Widget*>(pSender);
    string buttonname = btntmp->getName();
    switch(hash_(buttonname.c_str())){
        case "btn_left"_hash:
        {

        }
            break;
        case "btn_right"_hash:
        {

        }
            break;
        case "btn_buy"_hash:
        {

        }
            break;
        case "btn_back"_hash:
        {

        }
            break;
        default:
            break;
    }
}

void UIAttack::onWidgetTouchMove(cocos2d::Ref *pSender)
{
    Widget* btntmp = dynamic_cast<Widget*>(pSender);
    string buttonname = btntmp->getName();
    switch(hash_(buttonname.c_str())){
        case "btn_left"_hash:
        {

        }
            break;
        case "btn_right"_hash:
        {

        }
            break;
        case "btn_buy"_hash:
        {

        }
            break;
        case "btn_back"_hash:
        {

        }
            break;
        default:
            break;
    }
}

void UIAttack::onWidgetTouchEnd(cocos2d::Ref *pSender)
{
    Widget* btntmp = dynamic_cast<Widget*>(pSender);
    string buttonname = btntmp->getName();
    switch(hash_(buttonname.c_str())){
        case "btn_left"_hash:
        {

        }
            break;
        case "btn_right"_hash:
        {

        }
            break;
        case "btn_buy"_hash:
        {

        }
            break;
        case "btn_back"_hash:
        {

        }
            break;
        default:
            break;
    }
}

void UIAttack::onWidgetTouchCanceled(cocos2d::Ref *pSender)
{
    Widget* btntmp = dynamic_cast<Widget*>(pSender);
    string buttonname = btntmp->getName();
    switch(hash_(buttonname.c_str())){
        case "btn_left"_hash:
        {

        }
            break;
        case "btn_right"_hash:
        {

        }
            break;
        case "btn_buy"_hash:
        {

        }
            break;
        case "btn_back"_hash:
        {

        }
            break;
        default:
            break;
    }
}
//Panel
void UIAttack::initLayoutPanel_1()
{

}
void UIAttack::initLayoutlay_skillPanel()
{

}

void UIAttack::onEnter()
{
    Layer::onEnter();
    
}
void UIAttack::onExit()
{
    SpriteFrameCache::getInstance()->removeSpriteFramesFromFile("uiplist/UIAttack0.plist");
    Director::getInstance()->getTextureCache()->removeTextureForKey("uiplist/UIAttack0.png");

    Layer::onExit();
}
