//
//  UIAttack.h
//  game4
//
//  Created by Junpeng Zhang on 2/3/15.
//  本代码由工具生成
//
//资源加载适合cocos2d-x 3.2版本的cocostuido 1.6 for windows
//

#ifndef __game4__UIAttack__
#define __game4__UIAttack__

#include "cocos2d.h"
#include "ui/CocosGUI.h"
#include "editor-support/cocostudio/CocoStudio.h"
#include "BaseUILayer.h"

USING_NS_CC;
using namespace ui;
using namespace cocostudio;
class UIAttack : public BaseUILayer
{
protected:
    UIAttack();
public:
    virtual ~UIAttack();
    virtual void close(); //界面关闭
    //获取下次初始化界面时的参数数据,Ref可以是　　cocos2d字典(__Dictionary)，数组(__Array)，或者字符串(__String),或者其他继承自Ref的对象
    virtual cocos2d::Ref* getUIConfData();
    static UIAttack* createFromManger(Ref* dat);
    static UIAttack* create();
    static UIAttack* create(int uiID);
    virtual void onEnter();
    virtual void onExit();
    virtual bool init();
    Layout* m_rootLayout;
    
//button
    Button* m_btn_leftBtn; //Panel_1+btn_left,Panel+Button
    Button* m_btn_rightBtn; //Panel_1+btn_right,Panel+Button
    Button* m_btn_buyBtn; //Panel_1+btn_buy,Panel+Button
    Button* m_btn_backBtn; //Panel_1+btn_back,Panel+Button
//ImageView
    ImageView* m_img_uiattackBGImage; //Panel_1+img_uiattackBG,Panel+ImageView
    ImageView* m_img_frambgImage; //Panel_1+img_frambg,Panel+ImageView
    ImageView* m_img_tablebgImage; //Panel_1+img_tablebg,Panel+ImageView
    ImageView* m_img_mainbgImage; //Panel_1+img_mainbg,Panel+ImageView
    ImageView* m_img_selImage; //Panel_1+img_mainbg+img_sel,Panel+ImageView+ImageView
    ImageView* m_img_assistantbgImage; //Panel_1+img_assistantbg,Panel+ImageView
    ImageView* m_img_selImage; //Panel_1+img_assistantbg+img_sel,Panel+ImageView+ImageView
    ImageView* m_img_skillBGImage; //Panel_1+img_skillBG,Panel+ImageView
    ImageView* m_img_skill1Image; //Panel_1+lay_skillPanel+img_skill1,Panel+Panel+ImageView
    ImageView* m_img_skill2Image; //Panel_1+lay_skillPanel+img_skill2,Panel+Panel+ImageView
    ImageView* m_img_skill3Image; //Panel_1+lay_skillPanel+img_skill3,Panel+Panel+ImageView
    ImageView* m_img_txt_mainImage; //Panel_1+img_txt_main,Panel+ImageView
    ImageView* m_img_txt_assImage; //Panel_1+img_txt_ass,Panel+ImageView
//Panel
    Layout* m_lay_skillPanelLayout; //Panel_1+lay_skillPanel,Panel+Panel
    void initLayoutlay_skillPanel();

    void onTouchEvent(cocos2d::Ref *pSender, Widget::TouchEventType type);
    void onWidgetTouchBeigen(cocos2d::Ref *pSender);
    void onWidgetTouchMove(cocos2d::Ref *pSender);
    void onWidgetTouchEnd(cocos2d::Ref *pSender);
    void onWidgetTouchCanceled(cocos2d::Ref *pSender);


private:
    int m_uiID;
    
};

#endif /* defined(__game4__UIAttack__) */
    