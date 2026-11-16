def main():
    ft_list = ["Hello"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "Hello", "tutu!"}
    ft_dict = {"Hello": "titi!"}

    ft_list.append("World!")
    ft_tuple = ft_tuple[:-1] + ("Japan!",)
    ft_set.remove("tutu!")
    ft_set.add("Tokyo!")
    ft_dict["Hello"] = "42Tokyo!"

    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)


if __name__ == "__main__":
    main()
